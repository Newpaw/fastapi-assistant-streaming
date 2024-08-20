# FastAPI with OpenAI Assistant API Integration

## Overview

This project demonstrates how to integrate FastAPI with OpenAI's Assistant API, utilizing Server-Sent Events (SSE) for real-time streaming of responses. The application allows creating interactive sessions with an OpenAI Assistant, handling real-time data streaming, and showcasing how asynchronous communication can enhance user interaction.

## Features

- Assistant Setup: Configures OpenAI Assistant API.
- Thread Management: Create and manage conversation threads.
- Real-time Streaming: Utilize SSE for streaming from the OpenAI Assistant.
- Functionality Extension: Placeholder for future function calling integration.

## Getting Started

### Prerequisites

- Python 3.10+
- FastAPI
- Uvicorn (for running the application)
- OpenAI Python client

### Installation

Clone the repository:

```bash
git clone https://github.com/Newpaw/fastapi-assistant-streaming
cd fastapi-assistant-streaming
```

Install required packages:

```bash
pip install -r requirements.txt
```

Set up environment variables:
Create a `.env` file in the project root directory and add your OpenAI API key and Assistant ID:

```bash
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_ASSISTANT_ID=your_assistant_id_here
```

#### Obtaining OpenAI API Key and Assistant ID
To obtain the necessary credentials, follow these steps:

1. **Register and Log In to OpenAI**:
    - Go to [OpenAI Registration](https://platform.openai.com/signup) and create an account if you haven't already.
    - After registering, log in to your OpenAI account.

2. **Get Your OpenAI API Key**:
    - Navigate to the [API Keys](https://platform.openai.com/account/api-keys) page.
    - Click on "Create new key" and copy the generated API key. This will be used as your `OPENAI_API_KEY`.

3. **Create an Assistant and Get Assistant ID**:
    - Go to the [Assistants Page](https://platform.openai.com/assistants/asst_FsHCOcPyojYgJSKoBYQmAA9H).
    - Follow the instructions to create a new assistant.
    - Once the assistant is created, you'll receive an Assistant ID which you can find in the assistant’s details. This will be used as your `OPENAI_ASSISTANT_ID`.

Make sure to keep your `.env` file secure and do not share your API keys publicly.


### Running the Application

Start the FastAPI Development Server:

```bash
uvicorn main:app --reload
```

Or use dockerfile:

```bash
docker build -t fastapi-assistant-streaming .
docker run -p 8000:8000 fastapi-assistant-streaming
```

or 

```bash
docker run -p 8000:8000 --env-file .env newpaw/ai-webchat:latest
```

### Testing Endpoints

Check the Health:

```bash
curl -X 'GET' --url 'http://localhost:8000/healtcheck'
```

Get the Assistant:

```bash
curl -X 'GET' --url 'http://localhost:8000/api/v1/assistant'
```

Create a thread:

```bash
curl -X POST http://localhost:8000/api/v1/assistant/threads -H "Content-Type: application/json"
```

Send a message:

```bash
curl -N -X POST \
-H "Accept: text/event-stream" -H "Content-Type: application/json" \
-d '{"text": "Hello! Please introduce yourself", "thread_id": "thread_abc123" }' \
http://localhost:8000/api/v1/assistant/chat
```


## License

Distributed under the MIT License. See LICENSE for more information.

## Thanks to:
[xbreid](https://github.com/xbreid)