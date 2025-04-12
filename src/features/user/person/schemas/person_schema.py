from pydantic import BaseModel, ConfigDict
from uuid import UUID


class PersonCreateSchema(BaseModel):
    name: str
    email: str


class PersonResponseSchema(PersonCreateSchema):
    id: UUID

    model_config = ConfigDict(from_attributes=True)