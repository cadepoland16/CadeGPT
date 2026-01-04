CadeGPT

CadeGPT is a full-stack AI chat application built with FastAPI, a modern browser-based chat interface, and a pluggable large-language-model backend. It was designed to demonstrate how real AI products are built: with clean backend architecture, structured APIs, and a frontend that never talks directly to an AI model. The entire system runs locally using Ollama for free real-time inference, while remaining fully compatible with hosted providers such as OpenAI. Unlike simple demos, CadeGPT includes a real cloud database, meaning every conversation and message is permanently stored.

The application works by exposing a single backend endpoint at POST /api/chat. The web UI sends user messages to this endpoint, and the FastAPI backend creates or loads a conversation, routes the request to the correct language-model provider based on environment configuration, receives the AI response, stores both the user message and assistant reply in the database, and returns a structured response to the client. This allows the same frontend and API to work with mock models for testing, local models through Ollama for free inference, or paid hosted models without changing any UI or API code. This separation of concerns mirrors how production AI platforms are designed.

CadeGPT is built around a clean service-oriented architecture. The routing layer handles HTTP requests, the service layer coordinates chat logic, the database layer persists conversations and messages, and a dedicated provider layer communicates with the selected language model. Each AI response is wrapped in a structured object that includes not only the generated text but also metadata such as which model was used, which environment is running, the timestamp of the request, a unique request identifier, and the conversation ID. This makes logging, analytics, monitoring, and replay of conversations straightforward.

The frontend is a lightweight but fully functional chat interface that runs directly in the browser. It communicates exclusively with the FastAPI backend, rendering both user messages and assistant responses in real time. Because the UI depends only on the API, it remains stable regardless of which AI provider or database is used behind the scenes. This makes the system easy to extend, deploy, or upgrade without rewriting the frontend.

CadeGPT is intentionally designed around Supabase for persistent memory. Supabase provides a PostgreSQL database that stores conversations and messages, allowing CadeGPT to support real chat history, conversation continuity, and future user-level data. Every chat turn is written to the database, giving CadeGPT true memory instead of being a stateless chatbot. This transforms the project from a local AI demo into the foundation of a scalable SaaS-style AI platform.

The technology stack includes Python 3.13, FastAPI, Pydantic, Uvicorn, Supabase, Ollama, HTML, CSS, and vanilla JavaScript. The system is configured using environment variables so secrets are never committed to GitHub and AI providers or databases can be swapped without touching application code. The entire project is designed to be clean, modular, and easy to understand for both developers and recruiters reviewing the repository.

Future Improvements:

CadeGPT has been intentionally designed so that powerful features can be added without rewriting the system.

Planned future enhancements include:
	•	User authentication and accounts using Supabase Auth, allowing each user to have private conversations and saved chat history
	•	Multi-conversation management, including loading, renaming, and deleting past chats
	•	Conversation summaries and long-term memory so the AI can recall important facts across sessions
	•	Personalization, including system prompts, preferences, and user profiles
	•	Usage tracking and billing, enabling SaaS-style monetization
	•	Streaming AI responses for a more interactive chat experience
	•	Model switching and routing across multiple providers
	•	Better documentation, including comments, API reference pages, architecture diagrams, developer onboarding guides, and contribution guidelines
	•	Unit and integration testing, ensuring stability as the system grows

The current architecture already supports all of these upgrades — they can be added without breaking the existing UI, API, or database schema.

Requirements & Running Locally

CadeGPT is designed to be easy to run locally while following production-grade architecture patterns. The backend runs on FastAPI and Uvicorn, the AI model is provided by Ollama, and Supabase is used for persistent storage.

To run CadeGPT locally, the following are required:
	•	Python 3.13
	•	Ollama installed and running with a supported model (e.g., llama3.2)
	•	A Supabase project with a PostgreSQL database
	•	Environment variables configured in a .env file

The required environment variables are:
	•	SUPABASE_URL
	•	SUPABASE_ANON_KEY
	•	MODEL_PROVIDER (e.g., ollama)
	•	OLLAMA_MODEL (e.g., llama3.2)

Once dependencies are installed from requirements.txt and the .env file is configured, the application can be started with:

uvicorn app.main:app --reload --port 8000 --app-dir src

After the server starts, the chat interface is available at:

http://127.0.0.1:8000/chat

From there, users can send messages, receive AI responses, and browse conversation history stored in Supabase.

Project Purpose:

CadeGPT exists as both a learning platform and a portfolio-ready AI application. It demonstrates full-stack engineering, API design, AI system integration, cloud database persistence, and modern software architecture patterns. It is not a simple chatbot, but a well-structured AI platform that can evolve into a real product over time.

Built by Cade Poland. 