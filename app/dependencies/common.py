from app.services.assistant_service import AssistantService
from app.core.config import settings



def get_assistant_service() -> AssistantService:
    return AssistantService(use_azure=settings.USE_AZURE)
