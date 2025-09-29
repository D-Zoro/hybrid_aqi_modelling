# Operations Runbook

## Overview
This runbook captures standard operating procedures, alert response guidance, and escalation paths for the AiroSense platform. Update after every incident review.

## On-Call Contacts
- Primary: `@oncall-airflow` (PagerDuty schedule)
- Secondary: `@ml-ops`
- Escalation: Platform Engineering Manager

## Critical Services
| Service | Namespace | SLA | Notes |
| --- | --- | --- | --- |
| FastAPI Inference | `serving` | 99.5% monthly uptime | Autoscaled via HPA (CPU & latency) |
| Training Jobs | `training` | Daily completion by 04:00 UTC | Uses spot fallback |
| Data Ingestion Worker | `ingestion` | 98% successful runs per day | Retries, DLQ enabled |
| Feature Store | `shared` | 99% online read availability | Redis (online) + S3 (offline) |

## Alert Playbooks
### 1. Data Ingestion Failure
1. Acknowledge PagerDuty alert referencing `data_pipeline_failure` metric.
2. Inspect Celery/Temporal task logs for stack trace.
3. Re-run failed job via `scripts/rerun_ingestion.py --date <YYYY-MM-DD>`.
4. If API rate-limit exceeded, defer retry + update OpenWeather usage dashboard.
5. Post summary in `#airosense-ops`.

### 2. Model Performance Degradation
1. Triggered when MAE increases >15% vs trailing 7-day baseline.
2. Inspect `Grafana -> Model Performance` dashboard.
3. Review drift report at `s3://airosense-model-monitoring/drift/<date>.html`.
4. If drift confirmed, schedule expedited retraining job.
5. Notify product stakeholders with projected impact.

### 3. Inference Latency Spikes
1. Alert from `serving_latency_p95` > 1000ms for 15 min.
2. Check HPA scaling events and cluster node health.
3. Warm caches with `scripts/warm_cache.py` if cache hit ratio < 90%.
4. If model regression suspected, roll back via `mlflow models revert --version <prev>`.

## Standard Operating Procedures
- **Daily Health Check:** Review ingestion job status, training pipeline results, and inference error rates by 09:00 local time.
- **Weekly Maintenance:** Rotate API keys if expiring, prune old feature sets (>180 days) to Glacier.
- **Monthly:** Conduct chaos drill (simulate S3 outage) and update runbook with lessons learned.

## Incident Documentation
- Store incident postmortems in `docs/runbooks/incidents/<incident-id>.md`.
- Include timeline, root cause, remediation, follow-up tasks.

## Tooling References
- Grafana dashboards live under folder `AiroSense`.
- Kibana/Loki logs: query `trace_id` from API response header.
- Sentry project: `airosense-prod`.

## Appendices
- [Terraform State Recovery](../architecture/architecture.md#deployment-topology)
- [Model Registry Management Guide](../../backend/docs/model-registry.md) *(future addition)*
