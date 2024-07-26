from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "FastAPI Assistant API"
    OPENAI_API_KEY: str
    OPENAI_ASSISTANT_ID: str
    LOG_LEVEL: str = "INFO"
    PROJECT_VERSION: str = "1.0.1"
    firebase_type: str
    firebase_project_id: str
    firebase_private_key_id: str
    firebase_private_key: str
    firebase_client_email: str
    firebase_client_id: str
    firebase_auth_uri: str
    firebase_token_uri: str
    firebase_auth_provider_x509_cert_url: str
    firebase_client_x509_cert_url: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()


firebase_config = {
    "type": settings.firebase_type,
    "project_id": settings.firebase_project_id,
    "private_key_id": settings.firebase_private_key_id,
    "private_key": settings.firebase_private_key.replace("\\n", "\n"),
    "client_email": settings.firebase_client_email,
    "client_id": settings.firebase_client_id,
    "auth_uri": settings.firebase_auth_uri,
    "token_uri": settings.firebase_token_uri,
    "auth_provider_x509_cert_url": settings.firebase_auth_provider_x509_cert_url,
    "client_x509_cert_url": settings.firebase_client_x509_cert_url
}