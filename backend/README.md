# Backend

The backend consists of the trading and signaling bot with Telegram API integration.

## Project Structure

The backend is organized into two main directories:

### `app/` directory

Contains the FastAPI web application components:
- Web API endpoints and routing
- Authentication and user management
- Database models and ORM (SQLModel)
- Database connection and session management
- API documentation (Swagger/OpenAPI)

### `bot/` directory

Contains the core trading bot functionality:
- Trading strategies implementation
- Telegram bot integration
- Signal generation algorithms
- Exchange API connectors
- Trade execution logic

The `bot/` directory is further divided into:
- `signal/`: Crypto signals for price changes and important events sent to Telegram bot or notifications
- `trade/`: Crypto trade execution and analysis

## Backend Directory Structure

```
inure-bot/backend/
├── app/                # FastAPI web application
│   ├── main.py         # FastAPI app entry point
│   ├── database.py     # Database connection
│   ├── models.py       # SQLModel definitions
│   └── ...
├── bot/                # Trading bot implementation
│   ├── signal/         # Crypto signals for price changes and important events
│   ├── trade/          # Crypto trade execution and analysis 
├── pyproject.toml      # Project dependencies
└── run.py              # Application runner
```

## Development Setup

1. Create and activate a virtual environment:
```bash
uv venv
source .venv/Scripts/activate  # On Windows with Git Bash
```

2. Install dependencies:
```bash
uv pip install -e .
```

3. Run the application:
```bash
python run.py
```

The server will start at http://0.0.0.0:8000 with auto-reload enabled.
