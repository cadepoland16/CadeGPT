from fastapi import FastAPI
from app.routes.health import router as health_router
from app.routes.chat import router as chat_router
from pathlib import Path
from fastapi.staticfiles import StaticFiles
from app.routes.ui import router as ui_router

app = FastAPI(title="CadeGPT")

BASE_DIR = Path(__file__).resolve().parent  # src/app

app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")

app.include_router(ui_router)

# Health check route
app.include_router(health_router, prefix="/api")

# Chat route (OpenAI-powered)
app.include_router(chat_router, prefix="/api")