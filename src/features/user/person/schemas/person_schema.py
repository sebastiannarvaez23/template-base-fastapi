from pydantic import BaseModel, ConfigDict, Field, EmailStr
from uuid import UUID
from datetime import date
from fastapi import UploadFile
from typing import Optional


class PersonCreateSchema(BaseModel):
    first_name: str = Field(..., min_length=3, max_length=50)
    second_name: str = Field(..., min_length=3, max_length=50)
    first_last_name: str = Field(..., min_length=3, max_length=50)
    second_last_name: str = Field(..., min_length=3, max_length=50)
    phone: str = Field(..., min_length=10, max_length=10)
    email: EmailStr
    birth_date: date
    avatar: Optional[UploadFile] = None

    class Config:
        arbitrary_types_allowed = True
        from_attributes = True


class PersonResponseSchema(PersonCreateSchema):
    id: UUID

    model_config = ConfigDict(from_attributes=True)