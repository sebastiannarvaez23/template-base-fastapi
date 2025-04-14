import io

from config.minio import minio_conn
from config.config import settings
from datetime import timedelta
from minio.error import S3Error


class MinioClient:
    def __init__(self, bucket_name: str = settings.MNO_BUCKET_NAME):
        self.bucket_name = bucket_name
        self.ensure_bucket_exists()

    def ensure_bucket_exists(self):
        if not minio_conn.bucket_exists(self.bucket_name):
            minio_conn.make_bucket(self.bucket_name)

    def upload_file(self, file_data: bytes, file_name: str, content_type: str = "application/octet-stream") -> str:
        file_stream = io.BytesIO(file_data)
        file_size = len(file_data)

        minio_conn.put_object(
            bucket_name=self.bucket_name,
            object_name=file_name,
            data=file_stream,
            length=file_size,
            content_type=content_type
        )
        return file_name

    def get_presigned_url(self, file_name: str, expiry_minutes: int = 60) -> str:
        try:
            url = minio_conn.presigned_get_object(
                bucket_name=self.bucket_name,
                object_name=file_name,
                expires=timedelta(minutes=expiry_minutes)
            )
            return url
        except S3Error as e:
            raise Exception(f"Error generating presigned URL: {e}")

    def delete_file(self, file_name: str):
        try:
            minio_conn.remove_object(self.bucket_name, file_name)
        except S3Error as e:
            raise Exception(f"Error deleting file: {e}")
