from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class APIResponse(BaseModel):
    status: str = Field(default="success")
    message: Optional[str] = None
    timestamp: datetime = Field(default_factory=datetime.utcnow)
