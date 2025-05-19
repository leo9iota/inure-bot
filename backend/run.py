import uvicorn
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def main() -> None:
    """Run the application with Uvicorn server."""
    uvicorn.run(
        app="app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )

if __name__ == "__main__":
    main()
