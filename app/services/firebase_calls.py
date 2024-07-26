import firebase_admin
from firebase_admin import credentials, db
import asyncio
from app.core.config import firebase_config


# Path to the downloaded service account key
cred = credentials.Certificate(firebase_config)

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://safe-expert-default-rtdb.europe-west1.firebasedatabase.app'
})

# Function to send metrics to Firebase
def send_metrics(thread_id, metric_name, value):
    ref = db.reference(f'threads/{thread_id}')
    messages = ref.child(metric_name).get() or []
    messages.append(value)
    ref.child(metric_name).set(messages)

# Asynchronous wrapper for the synchronous send_metrics function
async def async_send_metrics(thread_id, metric_name, value):
    loop = asyncio.get_event_loop()
    await loop.run_in_executor(None, send_metrics, thread_id, metric_name, value)