# AiroSense Worker

Background jobs for data ingestion, batch predictions, and retraining orchestration.

## Local Development

```bash
poetry install
poetry run python app/worker.py
```

## Planned Jobs
- `jobs/ingest_satellite.py`
- `jobs/ingest_weather.py`
- `jobs/train_model.py`
- `jobs/batch_predict.py`
