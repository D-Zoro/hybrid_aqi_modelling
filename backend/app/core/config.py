from functools import lru_cache
from typing import List

from pydantic import AnyHttpUrl, Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_env: str = Field(default="local", alias="APP_ENV")
    api_v1_str: str = Field(default="/api/v1", alias="API_V1_STR")
    secret_key: str = Field(default="super-secret", alias="SECRET_KEY")
    allowed_origins: List[AnyHttpUrl] = Field(default_factory=list, alias="ALLOWED_ORIGINS")

    database_url: str = Field(alias="DATABASE_URL")
    redis_url: str = Field(alias="REDIS_URL")

    openweather_api_key: str = Field(alias="OPENWEATHER_API_KEY")
    gee_service_account_json_path: str = Field(alias="GEE_SERVICE_ACCOUNT_JSON_PATH")
    cpcb_api_token: str = Field(alias="CPCB_API_TOKEN")

    mlflow_tracking_uri: str = Field(alias="MLFLOW_TRACKING_URI")
    model_registry_s3_bucket: str = Field(alias="MODEL_REGISTRY_S3_BUCKET")
    feature_store_offline_path: str = Field(alias="FEATURE_STORE_OFFLINE_PATH")

    rate_limit_default: str = Field(default="60/minute", alias="RATE_LIMIT_DEFAULT")
    api_key_header_name: str = Field(default="X-API-Key", alias="API_KEY_HEADER_NAME")
    admin_api_key: str = Field(alias="ADMIN_API_KEY")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
