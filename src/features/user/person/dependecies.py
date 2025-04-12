from fastapi import Depends

from sqlalchemy.ext.asyncio import AsyncSession

from config.session import get_db
from features.user.person.adapters.repository.person_repository_impl import PersonRepositoryImpl
from features.user.person.application.services.person_service import PersonService
from features.user.person.domain.ports.person_repository import PersonRepository


def get_person_repository(db: AsyncSession = Depends(get_db)) -> PersonRepositoryImpl:
    return PersonRepositoryImpl(db)

def get_person_service(
    person_repository: PersonRepository = Depends(get_person_repository)
) -> PersonService:
    return PersonService(person_repository)