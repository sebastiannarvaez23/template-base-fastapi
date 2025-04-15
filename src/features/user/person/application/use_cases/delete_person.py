from uuid import UUID

from features.user.person.adapters.repository.person_repository_impl import PersonRepositoryImpl
from features.user.person.domain.entities.person import Person


class DeletePerson:
    def __init__(self, person_repository: PersonRepositoryImpl):
        self.person_repository = person_repository

    async def execute(self, person_id: UUID) -> bool:
        return await self.person_repository.delete(person_id)