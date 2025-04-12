from typing import Optional

from features.user.person.domain.ports.person_repository import PersonRepository
from features.user.person.domain.entities.person import Person


class GetPerson:
    def __init__(self, person_repository: PersonRepository):
        self.person_repository = person_repository

    async def execute(self, person_id: int) -> Optional[Person]:
        return self.person_repository.get_by_id(person_id)