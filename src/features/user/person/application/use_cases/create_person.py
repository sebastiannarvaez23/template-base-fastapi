from typing import Optional

from features.user.person.domain.entities.person import Person
from features.user.person.adapters.repository.person_repository_impl import PersonRepositoryImpl
from features.user.person.schemas.person_schema import PersonCreateSchema


class CreatePerson:
    def __init__(self, person_repository: PersonRepositoryImpl):
        self.person_repository = person_repository

    async def execute(self, person_data: PersonCreateSchema, avatar_filename: Optional[str] = None) -> Person:
        person_dict = person_data.dict()
        person_dict["avatar"] = avatar_filename
        person = await self.person_repository.create(person_dict)
        return person