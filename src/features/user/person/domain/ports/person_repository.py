from abc import ABC, abstractmethod
from typing import Optional

from features.user.person.domain.entities.person import Person


class PersonRepository(ABC):
    @abstractmethod
    def create(self, person: Person) -> Person:
        pass

    @abstractmethod
    def get_by_id(self, person_id: int) -> Optional[Person]:
        pass