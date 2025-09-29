from fastapi import APIRouter

from app.api.v1.routers import (  # noqa: F401  # imported for router inclusion
    data_collection,
    explain,
    management,
    predictions,
    training,
)

api_router = APIRouter()
api_router.include_router(predictions.router, prefix="/predictions", tags=["predictions"])
api_router.include_router(training.router, prefix="/training", tags=["training"])
api_router.include_router(management.router, prefix="/management", tags=["operations"])
api_router.include_router(data_collection.router, prefix="/data", tags=["data"])
api_router.include_router(explain.router, prefix="/explain", tags=["explainability"])
