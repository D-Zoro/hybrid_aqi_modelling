from typing import Any

from fastapi import APIRouter, Depends

from app.core.security import verify_api_key
from app.schemas.base import APIResponse

router = APIRouter()


@router.get("/health", response_model=APIResponse, summary="Service health")
async def service_health() -> APIResponse:
    return APIResponse(message="AiroSense backend healthy")


@router.get(
    "/status",
    response_model=dict[str, Any],
    summary="Runtime status summary",
    dependencies=[Depends(verify_api_key)],
)
async def service_status() -> dict[str, Any]:
    return {
        "uptime_seconds": 0,
        "model_version": "model-v0",
        "queued_jobs": 0,
    }
