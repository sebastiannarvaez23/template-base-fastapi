from fastapi import APIRouter, Depends
from fastapi import Query

from core.schemas.paginated_response import PaginatedResponse
from features.user.person.application.services.person_service import PersonService
from features.user.person.dependecies import get_person_service
from features.user.person.schemas.person_schema import PersonCreateSchema, PersonFilterSchema, PersonResponseSchema


router = APIRouter()

@router.get("/person", response_model=PaginatedResponse[PersonResponseSchema])
async def get_persons(
    page: int = Query(..., ge=1),
    filters: PersonFilterSchema = Depends(),
    person_service: PersonService = Depends(get_person_service)
):
    return await person_service.get_persons(page, filters)

@router.post("/person")
async def create_person(
    person_data: PersonCreateSchema,
    person_service: PersonService = Depends(get_person_service)
):
    return await person_service.create_person(person_data)