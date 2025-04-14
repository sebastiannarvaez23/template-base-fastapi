from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from config.session import get_db
from core.minio.minio_client import MinioClient
from features.user.person.adapters.repository.person_repository_impl import PersonRepositoryImpl

def get_minio_client() -> MinioClient:
    return MinioClient()

def get_person_repository(db: AsyncSession = Depends(get_db)) -> PersonRepositoryImpl:
    return PersonRepositoryImpl(db)

def get_person_service(
    person_repository: PersonRepositoryImpl = Depends(get_person_repository),
    minio_client: MinioClient = Depends(get_minio_client)
):
    from features.user.person.application.services.person_service import PersonService
    return PersonService(person_repository, minio_client)