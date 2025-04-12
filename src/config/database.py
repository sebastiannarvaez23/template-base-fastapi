import os

from sqlalchemy.ext.asyncio import create_async_engine


class DatabaseConfig:
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