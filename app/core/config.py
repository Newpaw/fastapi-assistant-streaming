from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "FastAPI Assistant API"
    OPENAI_API_KEY: str
    OPENAI_ASSISTANT_ID: str
    AZURE_BASE_URL: str
    AZURE_OPENAI_API_KEY: str
    AZURE_OPENAI_ASSISTANT_ID:str
    USE_AZURE: bool = True
    LOG_LEVEL: str = "INFO"
    PROJECT_VERSION: str = "1.0.1"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
