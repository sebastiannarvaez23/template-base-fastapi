from features.user.person.domain.entities.person import Person
from features.user.person.domain.ports.person_repository import PersonRepository
from features.user.person.schemas.person_schema import PersonCreateSchema, PersonResponseSchema


class PersonService:
    def __init__(self, person_repository: PersonRepository):
        self.person_repository = person_repository

    async def create_person(self, person_data: PersonCreateSchema) -> PersonResponseSchema:
        person: Person = await self.person_repository.create(person_data)
        person_dict = person.to_dict()
        return PersonResponseSchema(**person_dict)