from typing import List

from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    database_url: str = Field(default="sqlite:///./story.db", validation_alias="DATABASE_URL")
    api_prefix: str = Field(default="/api", validation_alias="API_PREFIX")
    debug: bool = Field(default=False, validation_alias="DEBUG")
    allowed_origins: List[str] = Field(default_factory=lambda: ["*"], validation_alias="ALLOWED_ORIGINS")
    openai_api_key: str = Field(default="", validation_alias="OPENAI_API_KEY")

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
    )

    @field_validator("allowed_origins", mode="before")
    def split_allowed_origins(cls, v):
        if isinstance(v, str):
            return [origin.strip() for origin in v.split(",") if origin.strip()]
        return v

    class config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True

settings = Settings()