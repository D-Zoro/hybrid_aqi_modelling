# syntax=docker/dockerfile:1.6

FROM python:3.11-slim AS base
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1
WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml /app
RUN pip install --no-cache-dir poetry==1.8.3 \
    && poetry config virtualenvs.create false \
    && poetry install --only main --no-root

FROM base AS dev
COPY . /app
RUN poetry install --no-root
CMD ["poetry", "run", "python", "app/worker.py"]

FROM base AS prod
COPY . /app
RUN poetry install --no-root --only main
CMD ["poetry", "run", "python", "app/worker.py"]
