import os

from fastapi import FastAPI
from sqlalchemy.ext.asyncio import create_async_engine
from features.user.person.adapters.http.person_routes import person_router


def init_routes(app: FastAPI):
    @app.get("/")
    async def root():
        return {"message": "API Gateway is running!"}
    app.include_router(person_router)

class DatabaseConfig:
    def __init__(self):
        self.database_url = os.getenv("DATABASE_URL")
        self.engine = create_async_engine(self.database_url, echo=True)

    async def authenticate(self):
        try:
            async with self.engine.begin() as conn:
                await conn.run_sync(lambda x: None)
            print("Database connected successfully.")
        except Exception as e:
            print(f"Database connection failed: {e}")
            raise