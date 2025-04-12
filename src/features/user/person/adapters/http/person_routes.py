from fastapi import APIRouter, Depends

from features.user.person.schemas.person_schema import PersonCreateSchema
from features.user.person.application.services.person_service import PersonService
from features.user.person.dependecies import get_person_service
from config.session import get_db


router = APIRouter()

@router.post("/person")
async def create_person(
    person_data: PersonCreateSchema,
    person_service: PersonService = Depends(get_person_service)
):
    return await person_service.create_person(person_data)