from fastapi import APIRouter, Depends

from features.user.person.schemas.person_schema import PersonCreateSchema
from features.user.person.application.services.person_service import PersonService
from features.user.person.adapters.repository.person_repository_impl import PersonRepositoryImpl
from sqlalchemy.ext.asyncio import AsyncSession
from config.session import get_db


router = APIRouter()

@router.post("/person")
async def create_person(user_data: PersonCreateSchema, db: AsyncSession = Depends(get_db)):
    person_repository = PersonRepositoryImpl(db)
    person_service = PersonService(person_repository)
    return await person_service.create_person(user_data)