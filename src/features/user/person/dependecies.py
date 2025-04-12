from fastapi import Depends
from config.session import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from features.user.person.adapters.repository.person_repository_impl import PersonRepositoryImpl
from features.user.person.application.services.person_service import PersonService

def get_person_service(db: AsyncSession = Depends(get_db)) -> PersonService:
    repo = PersonRepositoryImpl(db)
    return PersonService(repo)