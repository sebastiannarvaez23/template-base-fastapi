import asyncio

from fastapi import FastAPI

from dotenv import load_dotenv

from api_gateway.adapters.http.app_routes import init_routes
from config.database import DatabaseConfig
from config.server import Server
from config.session import init_db

load_dotenv()

app = FastAPI(
    title="Template base FastAPI",
    description="Template base for creating backends in fastapi.",
    version="1.0.0" 
)
init_routes(app)

@app.on_event("startup")
async def startup():
    db = DatabaseConfig()
    await db.authenticate()
    await init_db()

if __name__ == "__main__":
    server = Server(app)
    server.raise_server()
