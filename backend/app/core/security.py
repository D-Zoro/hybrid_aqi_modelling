from fastapi import Depends, Header, HTTPException, status

from app.core.config import settings


async def verify_api_key(x_api_key: str | None = Header(default=None, alias=settings.api_key_header_name)) -> None:
    if not x_api_key or x_api_key != settings.admin_api_key:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or missing API key")


def rate_limit_dependency() -> None:
    """Placeholder for rate limiter integration (FastAPI Limiter / Redis)."""
    return None
