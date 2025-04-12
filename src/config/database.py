import os

from sqlalchemy.ext.asyncio import create_async_engine


class DatabaseConfig:
    SQLALCHEMY_DATABASE_URL = os.getenv("DB_URL", "sqlite:///./test.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    def __init__(self):
        self.database_url = os.getenv("DB_URL")
        self.engine = create_async_engine(self.database_url, echo=True)

    async def authenticate(self):
        try:
            async with self.engine.begin() as conn:
                await conn.run_sync(lambda x: None)
            print("Database connected successfully.")
        except Exception as e:
            print(f"Database connection failed: {e}")
            raise
