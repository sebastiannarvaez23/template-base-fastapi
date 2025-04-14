from fastapi import APIRouter, Depends, Query, Path

from uuid import UUID

from core.schemas.paginated_response import PaginatedResponse
from features.user.person.application.services.person_service import PersonService
from features.user.person.dependecies import get_person_service
from features.user.person.schemas.person_schema import (
    PersonCreateSchema, 
    PersonFilterSchema, 
    PersonResponseSchema,
    PersonUpdateSchema
)


router = APIRouter()

@router.get("/person", response_model=PaginatedResponse[PersonResponseSchema])
async def get_persons(
    page: int = Query(..., ge=1),
    filters: PersonFilterSchema = Depends(),
    person_service: PersonService = Depends(get_person_service)
):
    return await person_service.get_persons(page, filters)

@router.get("/person/{person_id}", response_model=PersonResponseSchema)
async def get_person_by_id(
    person_id: UUID,
    person_service: PersonService = Depends(get_person_service)
):
    return await person_service.get_person_by_id(person_id)

@router.post("/person")
async def create_person(
    person_data: PersonCreateSchema,
    person_service: PersonService = Depends(get_person_service)
):
    return await person_service.create_person(person_data)

@router.put("/person/{person_id}", response_model=PersonResponseSchema)
async def update_person(
    person_id: UUID,
    person_data: PersonUpdateSchema,
    person_service: PersonService = Depends(get_person_service)
):
    return await person_service.update_person(person_id, person_data)

@router.delete("/person/{person_id}")
async def delete_person(
    person_id: UUID,
    person_service: PersonService = Depends(get_person_service)
):
    return await person_service.delete_person(person_id)