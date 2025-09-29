from fastapi import APIRouter, Depends

from app.core.security import verify_api_key
from app.schemas.base import APIResponse

router = APIRouter(dependencies=[Depends(verify_api_key)])


@router.post(
    "/collect",
    response_model=APIResponse,
    summary="Trigger ad-hoc data collection run",
)
async def collect_data() -> APIResponse:
    # TODO: enqueue ingestion workflow
    return APIResponse(message="Data collection job accepted")
