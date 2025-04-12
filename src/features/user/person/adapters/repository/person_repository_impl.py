from sqlalchemy.future import select
from typing import Optional

from features.user.person.domain.entities.person import Person
from features.user.person.domain.ports.person_repository import PersonRepository
from features.user.person.schemas.person_schema import PersonCreateSchema
from sqlalchemy.ext.asyncio import AsyncSession


class PersonRepositoryImpl(PersonRepository):
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, person_data: PersonCreateSchema) -> Person:
        person = Person(
            first_name=person_data.first_name,
            second_name=person_data.second_name,
            first_last_name=person_data.first_last_name,
            second_last_name=person_data.second_last_name,
            email=person_data.email,
            phone=person_data.phone,
            birth_date=person_data.birth_date,
            avatar=person_data.avatar,
        )
        self.db.add(person)
        await self.db.commit()
        return person

    async def get_by_id(self, person_id: int) -> Optional[Person]:
        result = await self.db.execute(select(Person).where(Person.id == person_id))
        return result.scalars().first()
