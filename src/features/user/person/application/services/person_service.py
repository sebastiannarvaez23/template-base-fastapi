from sqlalchemy.exc import IntegrityError
from uuid import UUID

from features.user.person.domain.entities.person import Person
from features.user.person.domain.exceptions.person_exceptions import PersonAlreadyExistsException, PhoneAlreadyExistsException, PersonNotFoundException
from features.user.person.domain.ports.person_repository import PersonRepository
from features.user.person.domain.utils.person_filter import PersonFilter
from features.user.person.schemas.person_schema import PersonCreateSchema, PersonResponseSchema
from utils.pagination.pagination_utils import paginate_query


class PersonService:
    def __init__(self, person_repository: PersonRepository):
        self.person_repository = person_repository
        
    async def get_persons(self, page: int, filters: dict):
        base_query = await self.person_repository.query()
        query = PersonFilter(**filters.dict()).apply(base_query)
        return await paginate_query(self.person_repository.db, query, page)
    
    async def get_person_by_id(self, person_id: UUID) -> PersonResponseSchema:
        person = await self.person_repository.get_by_id(person_id)
        if not person:
            raise PersonNotFoundException(person_id)
        return PersonResponseSchema.from_orm(person)

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