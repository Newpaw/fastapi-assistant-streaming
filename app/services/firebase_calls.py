import firebase_admin
from firebase_admin import credentials, db
import asyncio
from app.core.config import settings
from aiologger import Logger

logger = Logger.with_default_handlers(level=settings.LOG_LEVEL)

class FirebaseHandler:
    def __init__(self):
        self.initialized = False
        try:
            # Convert firebase_config to dictionary
            firebase_config = {
                "type": settings.firebase_type,
                "project_id": settings.firebase_project_id,
                "private_key_id": settings.firebase_private_key_id,
                "private_key": settings.firebase_private_key.replace('\\n', "\n"),
                "client_email": settings.firebase_client_email,
                "client_id": settings.firebase_client_id,
                "auth_uri": settings.firebase_auth_uri,
                "token_uri": settings.firebase_token_uri,
                "auth_provider_x509_cert_url": settings.firebase_auth_provider_x509_cert_url,
                "client_x509_cert_url": settings.firebase_client_x509_cert_url
            }

            # Use the dictionary directly with credentials.Certificate
            cred = credentials.Certificate(firebase_config)

            # Initialize the app with a service account, granting admin privileges
            firebase_admin.initialize_app(cred, {
                'databaseURL': 'https://safe-expert-default-rtdb.europe-west1.firebasedatabase.app'
            })
            self.initialized = True
        except Exception as e:
            logger.error(f"Error initializing Firebase: {e}")

    def send_metrics(self, thread_id, metric_name, value):
        if not self.initialized:
            logger.info("Firebase is not initialized.")
            return
        ref = db.reference(f'threads/{thread_id}')
        messages = ref.child(metric_name).get() or []
        messages.append(value)
        ref.child(metric_name).set(messages)

    async def async_send_metrics(self, thread_id, metric_name, value):
        if not self.initialized:
            logger.info("Firebase is not initialized.")
            return
        loop = asyncio.get_event_loop()
        await loop.run_in_executor(None, self.send_metrics, thread_id, metric_name, value)

    def is_initialized(self):
        logger.info(f"Firebase is initialized: {self.initialized}")
        return self.initialized