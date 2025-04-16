from fastapi import UploadFile

from datetime import date
from pydantic import BaseModel, ConfigDict, Field, EmailStr, validator
from typing import Optional
from uuid import UUID


class UserCreateSchema(BaseModel):
    nickname: str = Field(..., min_length=3, max_length=20)
    password: str = Field(..., min_length=3)
    lastAuth: Optional[date] = Field(None)
    origin: Optional[str] = Field(None, max_length=20)
    active: bool = Field(...)

    class Config:
        arbitrary_types_allowed = True
        from_attributes = True
        json_encoders = {
            date: lambda v: v.isoformat() if v else None
        }

    @validator('nickname')
    def nickname_no_spaces(cls, v):
        if ' ' in v:
            raise ValueError('Nickname cannot contain spaces')
        return v

class UserUpdateSchema(BaseModel):
    nickname: Optional[str] = Field(None, min_length=3, max_length=20)
    password: Optional[str] = Field(None, min_length=3)
    lastAuth: Optional[date] = None
    origin: Optional[str] = Field(None, max_length=20)
    active: Optional[bool] = None

    class Config:
        arbitrary_types_allowed = True
        from_attributes = True
        json_encoders = {
            date: lambda v: v.isoformat() if v else None
        }

class UserResponseSchema(BaseModel):
    id: UUID
    nickname: str
    lastAuth: Optional[date] = None
    origin: Optional[str] = None
    active: bool

    model_config = ConfigDict(
        from_attributes=True,
        json_encoders={
            date: lambda v: v.isoformat() if v else None
        }
    )

class UserFilterSchema(BaseModel):
    nickname: Optional[str] = None
    origin: Optional[str] = None
    active: Optional[bool] = None