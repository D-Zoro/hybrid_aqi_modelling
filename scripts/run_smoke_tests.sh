#!/usr/bin/env bash
set -euo pipefail

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

pushd "${PROJECT_ROOT}/backend" >/dev/null
poetry run pytest tests/test_health.py
popd >/dev/null

pushd "${PROJECT_ROOT}/frontend" >/dev/null
npm run lint
npm run test -- --watch=false
popd >/dev/null

printf "\nSmoke tests completed successfully.\n"
