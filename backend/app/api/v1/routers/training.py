from typing import Any

from fastapi import APIRouter, Depends, HTTPException

from app.core.security import verify_api_key
from app.schemas.base import APIResponse
from app.services.training_service import TrainingService

router = APIRouter(dependencies=[Depends(verify_api_key)])


@router.post("/train", response_model=APIResponse, summary="Trigger model training run")
async def trigger_training(service: TrainingService = Depends(TrainingService)) -> APIResponse:
    try:
        job_id = await service.start_training()
        return APIResponse(message=f"Training job {job_id} accepted")
    except Exception as exc:  # pragma: no cover
        raise HTTPException(status_code=500, detail=str(exc)) from exc


@router.post("/retrain", response_model=APIResponse, summary="Trigger retraining with latest data")
async def retrain(service: TrainingService = Depends(TrainingService)) -> APIResponse:
    job_id = await service.start_retraining()
    return APIResponse(message=f"Retraining job {job_id} accepted")


@router.get("/model-info", response_model=dict[str, Any], summary="Get model metadata")
async def model_info(service: TrainingService = Depends(TrainingService)) -> dict[str, Any]:
    return await service.get_model_metadata()
