from pydantic import BaseModel, ConfigDict, Field, EmailStr
from uuid import UUID


class PersonCreateSchema(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    email: EmailStr


class PersonResponseSchema(PersonCreateSchema):
    id: UUID

    model_config = ConfigDict(from_attributes=True)