from features.user.person.domain.entities.person import Person
from features.user.person.domain.ports.person_repository import PersonRepository
from features.user.person.schemas.person_schema import PersonCreateSchema


class CreatePerson:
    def __init__(self, user_repository: PersonRepository):
        self.user_repository = user_repository

    async def execute(self, user_data: PersonCreateSchema) -> Person:
        user = Person(name=user_data.name, email=user_data.email)
        return self.user_repository.create(user)