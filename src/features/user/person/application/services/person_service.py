from features.user.person.domain.ports.person_repository import PersonRepository
from features.user.person.schemas.person_schema import PersonCreateSchema, PersonResponseSchema


class PersonService:
    def __init__(self, person_repository: PersonRepository):
        self.person_repository = person_repository

    async def create_person(self, person_data: PersonCreateSchema) -> PersonResponseSchema:
        person = await self.person_repository.create(person_data)
        return PersonResponseSchema(
            id=person.id,
            name=person.name,
            email=person.email,
        )