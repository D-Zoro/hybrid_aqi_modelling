from typing import Any

from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException, UploadFile

from app.core.security import rate_limit_dependency, verify_api_key
from app.schemas.prediction import PredictionRequest, PredictionResponse
from app.services.prediction_service import PredictionService

router = APIRouter()


@router.post(
    "/predict",
    response_model=PredictionResponse,
    status_code=200,
    summary="Single point AQI prediction",
)
async def predict_single(
    payload: PredictionRequest,
    service: PredictionService = Depends(PredictionService),
    _: None = Depends(rate_limit_dependency),
) -> PredictionResponse:
    try:
        return await service.predict(payload)
    except Exception as exc:  # pragma: no cover - placeholder for structured errors
        raise HTTPException(status_code=500, detail=str(exc)) from exc


@router.post(
    "/batch",
    response_model=dict[str, Any],
    dependencies=[Depends(verify_api_key)],
    summary="Batch AQI predictions via payload",
)
async def predict_batch(
    payload: list[PredictionRequest],
    background_tasks: BackgroundTasks,
    service: PredictionService = Depends(PredictionService),
) -> dict[str, Any]:
    task_id = await service.queue_batch_prediction(payload, background_tasks)
    return {"status": "accepted", "task_id": task_id}


@router.post(
    "/upload",
    response_model=dict[str, Any],
    dependencies=[Depends(verify_api_key)],
    summary="Upload CSV for batch predictions",
)
async def predict_from_upload(
    file: UploadFile,
    service: PredictionService = Depends(PredictionService),
) -> dict[str, Any]:
    job = await service.process_uploaded_file(file)
    return {"status": "accepted", "job": job}
