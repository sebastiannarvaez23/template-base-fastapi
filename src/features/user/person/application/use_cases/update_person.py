from sqlalchemy.exc import IntegrityError
from uuid import UUID

from features.user.person.adapters.repository.person_repository_impl import PersonRepositoryImpl
from features.user.person.domain.entities.person import Person
from features.user.person.schemas.person_schema import PersonUpdateSchema


class UpdatePerson:
    def __init__(self, person_repository: PersonRepositoryImpl):
        self.person_repository = person_repository

    async def execute(self, person: Person, person_data: PersonUpdateSchema, avatar_filename: str) -> Person:
        person_data_dict = person_data.dict(exclude_unset=True)
        person_data_dict["avatar"] = avatar_filename
        return await self.person_repository.update(person, person_data_dict)