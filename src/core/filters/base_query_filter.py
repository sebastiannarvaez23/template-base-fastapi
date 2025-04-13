from typing import TypeVar, Generic
from sqlalchemy.sql import Select


T = TypeVar("T")

class BaseFilter(Generic[T]):
    def apply(self, query: Select) -> Select:
        return query