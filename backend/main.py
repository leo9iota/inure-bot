from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Session

from .database import create_db_and_tables, get_session
from .models import User, TradingBot, Trade

app = FastAPI(
    title="Inure Bot API",
    description="Crypto trading bot SaaS with Telegram integration",
    version="0.1.0",
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.get("/")
async def root():
    return {"message": "Welcome to Inure Bot API"}


@app.get("/health")
async def health_check():
    return {"status": "healthy"}
