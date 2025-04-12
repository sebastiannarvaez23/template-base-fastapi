from pydantic import BaseModel, ConfigDict


class PersonCreateSchema(BaseModel):
    name: str
    email: str


class PersonResponseSchema(PersonCreateSchema):
    id: int

    model_config = ConfigDict(from_attributes=True)