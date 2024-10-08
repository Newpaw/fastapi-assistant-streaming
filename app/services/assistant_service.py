import asyncio
import httpx
from openai import AsyncAzureOpenAI, AsyncOpenAI

from app.core.config import settings
from app.services.event_handler import EventHandler


class AssistantService:
    def __init__(self, use_azure: bool = False):
        """
        Initialize the AssistantService with either AsyncAzureOpenAI or AsyncOpenAI based on the flag.

        :param use_azure: A boolean flag to determine whether to use Azure OpenAI or OpenAI.
        """
        if use_azure:
            self.client = AsyncAzureOpenAI(
                api_key=settings.AZURE_OPENAI_API_KEY,
                azure_endpoint=settings.AZURE_BASE_URL,
                api_version="2024-05-01-preview"
            )
            self.assistant_id = settings.AZURE_OPENAI_ASSISTANT_ID
        else:
            self.client = AsyncOpenAI(api_key=settings.OPENAI_API_KEY)
            self.assistant_id = settings.OPENAI_ASSISTANT_ID

    async def get_assistant(self):
        assistant = await self.client.beta.assistants.retrieve(self.assistant_id)
        return assistant

    async def create_thread(self):
        thread = await self.client.beta.threads.create()
        if not thread.id:
            raise ValueError("Failed to create a valid thread.")
        
        return thread

    async def retrieve_thread(self, thread_id: str):
        thread = await self.client.beta.threads.retrieve(thread_id)
        return thread

    async def create_message(self, thread_id, content):
        message = await self.client.beta.threads.messages.create(
            thread_id=thread_id,
            role="user",
            content=content,
        )
        return message

    async def run_stream(self, thread, stream_it: EventHandler):
        try:
            async with self.client.beta.threads.runs.stream(
                thread_id=thread.id,
                assistant_id=self.assistant_id,
                event_handler=stream_it,
            ) as stream:
                await stream.until_done()
        except httpx.HTTPStatusError as e:
            if e.response.status_code == 404:
                print("Thread or endpoint not found. Verify thread ID and assistant ID.")
            raise

    async def create_gen(self, thread, stream_it: EventHandler):
        task = asyncio.create_task(self.run_stream(thread, stream_it))
        async for token in stream_it.aiter():
            yield token
        await task
