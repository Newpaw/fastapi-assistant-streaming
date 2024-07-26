from app.services.assistant_service import AssistantService
from app.services.firebase_calls import FirebaseHandler


def get_assistant_service() -> AssistantService:
    return AssistantService()


def get_firebase_service()-> FirebaseHandler:
    return FirebaseHandler()