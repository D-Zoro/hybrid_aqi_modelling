#!/usr/bin/env bash
set -euo pipefail

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

pushd "${PROJECT_ROOT}" >/dev/null

if ! command -v docker-compose >/dev/null 2>&1; then
  echo "docker-compose is required. Install Docker Desktop or docker compose plugin." >&2
  exit 1
fi

export COMPOSE_PROJECT_NAME=airosense

cat <<EOF
Starting AiroSense local stack:
- Backend: http://localhost:8000/docs
- Frontend: http://localhost:3000
- Postgres: localhost:5432 (user: airosense / password: change-me)
- Redis: localhost:6379
EOF

docker compose up -d --build

popd >/dev/null
