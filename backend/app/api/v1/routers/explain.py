from fastapi import APIRouter, Depends

from app.core.security import verify_api_key
from app.schemas.base import APIResponse

router = APIRouter(dependencies=[Depends(verify_api_key)])


@router.get("/latest", response_model=dict[str, str], summary="Latest explainability artifact")
async def explain_latest() -> dict[str, str]:
    return {
        "artifact_uri": "s3://airosense-explainability/latest/shap_summary.png",
        "generated_at": "2025-01-01T00:00:00Z",
    }


@router.post("/generate", response_model=APIResponse, summary="Generate on-demand explanations")
async def generate_explanations() -> APIResponse:
    # TODO: trigger background SHAP job
    return APIResponse(message="Explainability job accepted")
