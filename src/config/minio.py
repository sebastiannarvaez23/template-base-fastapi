from minio import Minio
from config.config import settings


minio_conn = Minio(
    f"{settings.MNO_ENDPOINT}:{settings.MNO_PORT}",
    access_key=settings.MNO_ACCESS_KEY,
    secret_key=settings.MNO_SECRET_KEY,
    secure=settings.MNO_SECURE
)