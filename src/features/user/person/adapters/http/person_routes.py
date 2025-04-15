from fastapi import APIRouter, Depends, Query, File, UploadFile, Form

from datetime import date
from pydantic import EmailStr
from typing import Optional
from uuid import UUID

from core.schemas.paginated_response import PaginatedResponse
from features.user.person.application.services.person_service import PersonService
from features.user.person.person_di import get_person_service
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

@router.post("/person", response_model=PersonResponseSchema)
async def create_person(
    first_name: str = Form(...),
    second_name: Optional[str] = Form(None),
    first_last_name: str = Form(...),
    second_last_name: Optional[str] = Form(None),
    email: EmailStr = Form(...),
    phone: str = Form(...),
    birth_date: date = Form(...),
    avatar: Optional[UploadFile] = File(None),
    person_service: PersonService = Depends(get_person_service)
):
    person_data = PersonCreateSchema(
        first_name=first_name,
        second_name=second_name,
        first_last_name=first_last_name,
        second_last_name=second_last_name,
        email=email,
        phone=phone,
        birth_date=birth_date,
        avatar=avatar
    )

    return await person_service.create_person(person_data, avatar)

@router.put("/person/{person_id}", response_model=PersonResponseSchema)
async def update_person(
    person_id: UUID,
    first_name: Optional[str] = Form(None),
    second_name: Optional[str] = Form(None),
    first_last_name: Optional[str] = Form(None),
    second_last_name: Optional[str] = Form(None),
    email: Optional[EmailStr] = Form(None),
    phone: Optional[str] = Form(None),
    birth_date: Optional[date] = Form(None),
    avatar: Optional[UploadFile] = File(None),
    person_service: PersonService = Depends(get_person_service)
):
    person_data = PersonUpdateSchema(
        first_name=first_name,
        second_name=second_name,
        first_last_name=first_last_name,
        second_last_name=second_last_name,
        email=email,
        phone=phone,
        birth_date=birth_date
    )
    return await person_service.update_person(person_id, person_data, avatar)

@router.delete("/person/{person_id}")
async def delete_person(
    person_id: UUID,
    person_service: PersonService = Depends(get_person_service)
):
    return await person_service.delete_person(person_id)