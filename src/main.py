from fastapi import FastAPI

from dotenv import load_dotenv

from api_gateway.adapters.http.app_routes import init_routes
from config.database import DatabaseConfig
from config.server import Server


load_dotenv()

app = FastAPI()
init_routes(app)

@app.on_event("startup")
async def startup():
    db = DatabaseConfig()
    await db.authenticate()

if __name__ == "__main__":
    server = Server(app)
    server.raise_server()