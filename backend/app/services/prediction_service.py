from __future__ import annotations

import csv
import io
import json
from typing import Any, Iterable

from fastapi import UploadFile

from app.schemas.prediction import PredictionRequest, PredictionResponse


class PredictionService:
    """Service layer handling inference requests."""

    def __init__(self) -> None:
        # TODO: inject model registry, feature store, and cache clients
        self.model_version = "model-v0"

    async def predict(self, request: PredictionRequest) -> PredictionResponse:
        # Placeholder logic: generate synthetic prediction
        dummy_prediction = {
            "timestamp_utc": request.timestamp_utc,
            "aqi": 120.0,
            "aqi_category": "Unhealthy",
            "pm25_ug_m3": 85.0,
            "pm10_ug_m3": 160.0,
            "no2_ug_m3": 45.0,
        }
        return PredictionResponse(
            request=request,
            predictions=[dummy_prediction],
            model_version=self.model_version,
        )

    async def queue_batch_prediction(
        self,
        payloads: Iterable[PredictionRequest],
        background_tasks: Any,
    ) -> str:
        # In prod, enqueue Celery/Temporal task. For now log + return placeholder ID.
        background_tasks.add_task(self._process_batch_sync, list(payloads))
        return "batch-job-placeholder"

    async def process_uploaded_file(self, file: UploadFile) -> dict[str, Any]:
        contents = await file.read()
        reader = csv.DictReader(io.StringIO(contents.decode("utf-8")))
        records = [row for row in reader]
        # TODO: validate schema, convert to PredictionRequest instances
        return {"records": len(records), "job_id": "upload-job-placeholder"}

    def _process_batch_sync(self, payloads: list[PredictionRequest]) -> None:
        # Placeholder for background batch processing
        _ = json.dumps([payload.model_dump() for payload in payloads])
        return None
