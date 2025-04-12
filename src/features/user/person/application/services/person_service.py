from sqlalchemy.exc import IntegrityError

from features.user.person.domain.entities.person import Person
from features.user.person.domain.ports.person_repository import PersonRepository
from features.user.person.schemas.person_schema import PersonCreateSchema, PersonResponseSchema
from features.user.person.domain.exceptions.person_exceptions import (
    PersonAlreadyExistsException,
    PhoneAlreadyExistsException
)

class PersonService:
    def __init__(self, person_repository: PersonRepository):
        self.person_repository = person_repository

    async def create_person(self, person_data: PersonCreateSchema) -> PersonResponseSchema:
        try:
            person: Person = await self.person_repository.create(person_data)
        except IntegrityError as e:
            if "email" in str(e.orig).lower():
                raise PersonAlreadyExistsException(person_data.email)
            elif "phone" in str(e.orig).lower():
                raise PhoneAlreadyExistsException(person_data.phone)
            else:
                raise
        return PersonResponseSchema.from_orm(person)