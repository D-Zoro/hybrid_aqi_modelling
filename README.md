# AiroSense

> **Tagline:** Near-real-time air quality forecasting from sky to street.

AiroSense is an end-to-end air pollution prediction platform that fuses Sentinel-5P satellite observations, OpenWeather meteorological forecasts, and CPCB/OpenAQ ground monitors to serve actionable AQI predictions, insights, and alerts for India and beyond. The project ships with production-ready infrastructure automation, typed APIs, a modern web front-end, MLOps workflows, and operational runbooks.

## Quick Links
- [Architecture Overview](./docs/architecture/architecture.md)
- [Runbooks](./docs/runbooks/operations.md)
- [Data Dictionary](./docs/data/data-dictionary.md)
- [Backend App](./backend/README.md)
- [Frontend App](./frontend/README.md)
- [Worker Jobs](./worker/README.md)
- [Infrastructure](./infra/terraform)

## Local Development Snapshot
- Compose stack at `docker-compose.yml` provides backend (`http://localhost:8000`), frontend (`http://localhost:3000`), worker, Postgres, and Redis.
- Synthetic dataset generator located at `backend/scripts/generate_synthetic_data.py`.
- Make-style helper scripts live in `scripts/`.

## Alternate Project Names
1. **Atmosight**
2. **Skylumen AQ**
3. **PolluCast**
