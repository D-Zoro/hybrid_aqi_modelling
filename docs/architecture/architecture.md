# AiroSense Architecture Overview

## System Summary
AiroSense provides end-to-end ingestion, processing, modeling, serving, and monitoring for air pollution predictions by fusing Sentinel-5P satellite imagery, weather data from OpenWeather, and CPCB/OpenAQ ground-truth measurements. The platform is deployed on AWS with containerized workloads orchestrated by Kubernetes (EKS) and automated via Terraform. Models are trained offline with scheduled retraining jobs and served through a low-latency FastAPI service exposed via an API gateway. Observability is powered by OpenTelemetry, Prometheus, Grafana, and Sentry.

## Logical Components

- **Data Ingestion Layer**
  - Satellite Connector (Google Earth Engine)
  - Weather Connector (OpenWeather)
  - Ground Truth Connector (CPCB/OpenAQ APIs)
  - Ingestion Orchestrator (Temporal/Celery worker)
  - Landing Storage (S3 raw zone)
  - Metadata Store (PostgreSQL / TimescaleDB)

- **Processing & Feature Engineering**
  - Preprocessing Jobs (Spark/EMR or Pandas on ECS Fargate for MVP)
  - Feature Store (Feast backed by S3 + Redis) with semantic layers
  - Data Quality Engine (Great Expectations) enforcing validation rules

- **Modeling Platform**
  - Training Jobs (scikit-learn, LightGBM, XGBoost) orchestrated by SageMaker or custom Kubernetes jobs
  - Experiment Tracking (MLflow) with model registry
  - Hyperparameter Tuning (Optuna) triggered via scheduled pipelines

- **Serving Layer**
  - FastAPI inference service packaged with ONNX Runtime
  - Batch prediction worker (Kubernetes CronJob)
  - Redis cache for hot predictions & feature lookups
  - API Gateway + WAF for secure access

- **Observability & Ops**
  - OpenTelemetry traces, Prometheus metrics, and Loki logs aggregated into Grafana
  - Alerting through PagerDuty/Slack based on performance and data pipelines
  - Runbooks stored in `docs/runbooks`

## Data Flow Summary
1. **Ingestion:** Scheduled worker pulls Sentinel-5P data via Google Earth Engine API, weather data via OpenWeather One Call API, and CPCB station data. Raw JSON/GeoTIFF files are stored in `s3://airosense-data/raw/{source}/{yyyy}/{mm}/{dd}/`.
2. **Validation:** Great Expectations suite validates schema, completeness, and cross-source consistency. Failures trigger alerts and park data in `raw/quarantine/`.
3. **Processing:** Transformation jobs standardize units, interpolate missing values, align temporal granularity (hourly), and enrich with geospatial features. Output parquet files in `s3://airosense-data/processed/{region}/{yyyy}/{mm}/{dd}/`.
4. **Feature Engineering:** Feature jobs compute rolling windows, lag features, meteorological indices, and encode station metadata. Features registered in Feast with online store Redis and offline store S3 Parquet.
5. **Training:** Orchestrated by MLflow pipeline triggered daily. Models saved as ONNX and versioned in registry. Evaluation metrics stored alongside artifacts.
6. **Serving:** FastAPI service loads latest production model from registry, fetches features via Feast online store, and returns predictions. Batch jobs write predictions to TimescaleDB and expose via API.
7. **Monitoring:** Prediction logs, drift metrics, and data quality KPIs sent to Prometheus/Loki and visualized in Grafana. Alerts route to on-call via PagerDuty.

## Deployment Topology
- **VPC:** Private subnets for EKS nodes, public subnets for ALB.
- **EKS Cluster:** Namespace isolation for `ingestion`, `training`, `serving`, `ops`.
- **Managed Databases:** AWS RDS (PostgreSQL/TimescaleDB), ElastiCache Redis, S3 buckets for storage.
- **CI/CD:** GitHub Actions pushes container images to ECR, applies Terraform and Helm charts to deploy.

## Security Considerations
- IAM roles scoped per workload with least privilege (e.g., read-only GEE, read/write S3 buckets).
- Secrets stored in AWS Secrets Manager and injected via Kubernetes secrets.
- API gateway enforces TLS 1.2+, rate limiting, and WAF rules.
- Audit logging enabled for API access and model operations.

## Cost Controls
- Use spot instances for training workloads and dev clusters.
- Archive historical data older than 6 months to S3 Glacier.
- Cache frequent weather requests to reduce API costs.
- Auto-scale inference pods based on CPU/latency thresholds.
