# AiroSense Backend

FastAPI-based backend powering inference, training orchestration, data ingestion, and monitoring APIs for AiroSense.

## Features
- Typed FastAPI endpoints with Pydantic v2 models
- Modular services for predictions, training, data collection, explainability
- Celery worker integration for asynchronous jobs
- ML components (Feast, MLflow, ONNX Runtime) for production-grade MLOps

## Local Development

```bash
poetry install
poetry run uvicorn app.main:app --reload
```

Visit `http://localhost:8000/docs` for OpenAPI docs.

## Tests

```bash
poetry run pytest
```

## Environment Variables
See `.env.example` for required configuration, including database URL, Redis, GEE credentials, and API keys.
