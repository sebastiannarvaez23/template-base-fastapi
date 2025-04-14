from fastapi import UploadFile
from datetime import date
from pydantic import BaseModel, ConfigDict, Field, EmailStr
from typing import Optional
from uuid import UUID


class PersonCreateSchema(BaseModel):
    first_name: str = Field(..., min_length=3, max_length=50)
    second_name: Optional[str] = Field(None, min_length=3, max_length=50)
    first_last_name: str = Field(..., min_length=3, max_length=50)
    second_last_name: Optional[str] = Field(None, min_length=3, max_length=50)
    phone: str = Field(..., min_length=10, max_length=10)
    email: EmailStr
    birth_date: date
    avatar: Optional[UploadFile] = None

    class Config:
        arbitrary_types_allowed = True
        from_attributes = True

class PersonUpdateSchema(BaseModel):
    first_name: Optional[str] = Field(None, min_length=3, max_length=50)
    second_name: Optional[str] = Field(None, min_length=3, max_length=50)
    first_last_name: Optional[str] = Field(None, min_length=3, max_length=50)
    second_last_name: Optional[str] = Field(None, min_length=3, max_length=50)
    phone: Optional[str] = Field(None, min_length=10, max_length=10)
    email: Optional[EmailStr] = None
    birth_date: Optional[date] = None
    avatar: Optional[UploadFile] = None

    class Config:
        arbitrary_types_allowed = True
        from_attributes = True

class PersonResponseSchema(PersonCreateSchema):
    id: UUID
    model_config = ConfigDict(from_attributes=True)
    
class PersonFilterSchema(BaseModel):
    first_name: Optional[str] = None
    second_name: Optional[str] = None
    first_last_name: Optional[str] = None
    second_last_name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None