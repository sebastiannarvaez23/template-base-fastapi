from fastapi import UploadFile,Form
from datetime import date
from pydantic import BaseModel, ConfigDict, Field, EmailStr
from typing import Optional
from uuid import UUID


class PersonCreateForm(BaseModel):
    first_name: str
    second_name: Optional[str] = None
    first_last_name: str
    second_last_name: Optional[str] = None
    email: str
    phone: str
    birth_date: str

    @classmethod
    def as_form(
        cls,
        first_name: str = Form(...),
        second_name: Optional[str] = Form(None),
        first_last_name: str = Form(...),
        second_last_name: Optional[str] = Form(None),
        email: str = Form(...),
        phone: str = Form(...),
        birth_date: str = Form(...)
    ):
        return cls(
            first_name=first_name,
            second_name=second_name or None,
            first_last_name=first_last_name,
            second_last_name=second_last_name or None,
            email=email,
            phone=phone,
            birth_date=birth_date,
        )



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



class PersonResponseSchema(BaseModel):
    id: UUID
    first_name: str
    second_name: Optional[str]
    first_last_name: str
    second_last_name: Optional[str]
    phone: str
    email: EmailStr
    birth_date: date
    avatar: Optional[str] = None  

    model_config = ConfigDict(from_attributes=True)



class PersonFilterSchema(BaseModel):
    first_name: Optional[str] = None
    second_name: Optional[str] = None
    first_last_name: Optional[str] = None
    second_last_name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None