from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    MNO_BUCKET_NAME: str = "tebafa"
    MINIO_ENDPOINT: str = "localhost"
    MINIO_PORT: int = 9000
    MINIO_ACCESS_KEY: str = "minio"
    MINIO_SECRET_KEY: str = "minio123"
    MNO_BUCKET_NAME: str = "tebafa"
    MINIO_SECURE: bool = False
    

    class Config:
        env_file = ".env"

settings = Settings()