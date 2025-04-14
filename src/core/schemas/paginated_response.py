from typing import Generic, TypeVar, List
from pydantic import BaseModel
from pydantic.generics import GenericModel


T = TypeVar("T")

class PaginatedResponse(GenericModel, Generic[T]):
    count: int
    rows: List[T]