CadeGPT

CadeGPT is a full-stack AI chat application built with FastAPI, Ollama, and a modern browser-based chat interface. It demonstrates how to design and implement a production-style large language model backend with clean architecture, provider abstraction, and a real frontend, while remaining completely free to run locally.
The application allows users to chat with an AI through a web interface. The frontend sends requests to a FastAPI backend, which routes each request to the appropriate language model provider based on environment configuration. This mirrors how real AI platforms are designed in production systems.

What CadeGPT Does:
-CadeGPT provides a web-based chat UI similar to ChatGPT.
-It exposes a REST API endpoint at POST /api/chat.
-It supports multiple LLM providers through environment-based routing.
-It returns structured responses that include the model, environment, timestamp, and request ID.

The frontend never talks directly to a language model. All communication flows through the FastAPI backend, which provides a single stable interface and makes the system easy to extend.

LLM Provider System:
    The backend supports multiple language model providers:
    -Mock: Used for testing the UI and backend without any model.
    -Ollama: Uses a local large language model running on the developer’s machine. This allows real AI responses with no API costs and no internet dependency.
    -OpenAI API Key (optional due to financial needs): Can be enabled later for production-grade hosted models without changing any frontend code.

The active provider is controlled by the .env file using the LLM_PROVIDER variable. This makes CadeGPT flexible and future-proof.

Architecture Overview:
-Browser (Chat UI)
-FastAPI Backend (POST /api/chat)
-Chat Service (provider router)
-Mock provider, Ollama, or OpenAI

Key architectural principles:
-The frontend never calls a model directly.
-All AI traffic goes through the backend.
-Providers are swappable without breaking the UI.
-Responses are standardized and structured.

Technology Stack:
    Backend:
        -Python 3.9
        -FastAPI
        -Pydantic
        -Uvicorn
        -python-dotenv
    AI:
        -Ollama for local inference
        -Pluggable provider abstraction
    Frontend:
        -HTML
        -CSS
        -Vanilla JavaScript
        -Served by FastAPI templates

Development:
-Virtualenv
-GitHub version control
-Environment-based configuration

Structured API Responses:
Each call to POST /api/chat returns a JSON object that includes the AI reply along with metadata such as which model was used, which environment is running, a timestamp, and a unique request ID. This design makes it easy to log conversations, store them in a database, and analyze usage later.

Planned Supabase Integration:
CadeGPT is designed to be extended into a real product using Supabase.

Supabase will provide:
-User authentication
-A PostgreSQL database
-An API layer
-A free hosting tier

Planned database tables:
-Users
-Conversations
-Messages
-Model usage

This will enable persistent chat history, user accounts, conversation memory, and usage analytics. Supabase also makes it easy to add paid tiers later without changing the core architecture.

Running CadeGPT Locally:
-Install Ollama.
-Pull a model such as llama3.2.
-Set your .env file with the Ollama provider, base URL, and model name.
-Start the backend using uvicorn.
-Open the chat UI at http://127.0.0.1:8000/chat.

Why This Project Matters:
CadeGPT demonstrates full-stack AI system design, API-driven architecture, LLM provider abstraction, local AI inference, and frontend-backend integration. It is designed as a scalable foundation for a real AI product, not just a simple chatbot.

Built by Cade Poland.