from abc import ABC, abstractmethod
from typing import Optional
from sqlalchemy.sql import Select

from features.user.person.domain.entities.person import Person


class PersonRepository(ABC):
    
    @abstractmethod
    async def query(self) -> Select:
        pass
    
    @abstractmethod
    def get_by_id(self, person_id: int) -> Optional[Person]:
        pass
    
    @abstractmethod
    def create(self, person: Person) -> Person:
        pass
