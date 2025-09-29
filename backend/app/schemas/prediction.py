from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field


class Coordinate(BaseModel):
    latitude: float = Field(ge=-90, le=90)
    longitude: float = Field(ge=-180, le=180)


class PredictionRequest(BaseModel):
    coordinates: Coordinate
    timestamp_utc: datetime = Field(description="ISO8601 timestamp for prediction horizon")
    horizon_hours: int = Field(default=1, ge=1, le=72)
    include_explanations: bool = False


class PredictionPoint(BaseModel):
    timestamp_utc: datetime
    aqi: float
    aqi_category: str
    pm25_ug_m3: Optional[float]
    pm10_ug_m3: Optional[float]
    no2_ug_m3: Optional[float]


class PredictionResponse(BaseModel):
    request: PredictionRequest
    predictions: List[PredictionPoint]
    model_version: str
    generated_at: datetime = Field(default_factory=datetime.utcnow)
