from sqlalchemy.ext.asyncio import AsyncSession

from core.repository.base_repository import BaseRepository
from features.user.person.domain.entities.person import Person
from features.user.person.schemas.person_schema import PersonCreateSchema, PersonUpdateSchema


class PersonRepositoryImpl(BaseRepository[Person, PersonCreateSchema, PersonUpdateSchema]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, Person)