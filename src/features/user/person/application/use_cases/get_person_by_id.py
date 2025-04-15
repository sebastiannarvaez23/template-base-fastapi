from typing import Optional
from uuid import UUID

from features.user.person.adapters.repository.person_repository_impl import PersonRepositoryImpl
from features.user.person.domain.entities.person import Person


class GetPersonById:
    def __init__(self, person_repository: PersonRepositoryImpl):
        self.person_repository = person_repository

    async def execute(self, person_id: UUID) -> Optional[Person]:
        return await self.person_repository.get_by_id(person_id)