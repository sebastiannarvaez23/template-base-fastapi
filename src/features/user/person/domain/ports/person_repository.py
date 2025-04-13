from abc import ABC, abstractmethod
from sqlalchemy.sql import Select
from typing import Optional
from uuid import UUID

from features.user.person.domain.entities.person import Person


class PersonRepository(ABC):
    
    @abstractmethod
    async def query(self) -> Select:
        pass
    
    @abstractmethod
    def get_by_id(self, person_id: UUID) -> Optional[Person]:
        pass
    
    @abstractmethod
    def create(self, person: Person) -> Person:
        pass
