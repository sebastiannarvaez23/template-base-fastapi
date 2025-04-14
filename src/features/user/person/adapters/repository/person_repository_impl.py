from sqlalchemy.ext.asyncio import AsyncSession

from features.user.person.domain.entities.person import Person
from features.user.person.schemas.person_schema import PersonCreateSchema, PersonUpdateSchema
from core.repository.base_repository import BaseRepository


class PersonRepositoryImpl(BaseRepository[Person, PersonCreateSchema, PersonUpdateSchema]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, Person)