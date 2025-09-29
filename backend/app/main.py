from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette_exporter import PrometheusMiddleware, handle_metrics

from app.api.v1.routes import api_router
from app.core.config import settings
from app.core.logging import configure_logging

configure_logging()

app = FastAPI(
    title="AiroSense API",
    description="AI-driven air pollution prediction platform",
    version="0.1.0",
    openapi_tags=[
        {"name": "predictions", "description": "Model inference endpoints"},
        {"name": "operations", "description": "System health and metadata"},
        {"name": "training", "description": "Model training workflows"},
        {"name": "data", "description": "Data ingestion and inspection"},
        {"name": "explainability", "description": "Model interpretability"},
    ],
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.add_middleware(
    PrometheusMiddleware,
    app_name="airosense-api",
    group_paths=True,
    prefix="airosense",
)

app.add_route("/metrics", handle_metrics)

app.include_router(api_router, prefix=settings.api_v1_str)


@app.get("/health", tags=["operations"], summary="Service health")
async def read_health() -> dict[str, str]:
    return {"status": "ok"}
