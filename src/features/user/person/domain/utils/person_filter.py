from sqlalchemy.sql import Select

from core.filters.base_query_filter import BaseFilter
from features.user.person.domain.entities.person import Person


class PersonFilter(BaseFilter[Person]):
    def __init__(self, first_name=None, second_name=None, email=None, phone=None, **kwargs):
        self.first_name = first_name
        self.second_name = second_name
        self.email = email
        self.phone = phone

    def apply(self, query: Select) -> Select:
        if self.first_name:
            query = query.where(Person.first_name.ilike(f"%{self.first_name}%"))
        if self.second_name:
            query = query.where(Person.second_name.ilike(f"%{self.second_name}%"))
        if self.email:
            query = query.where(Person.email.ilike(f"%{self.email}%"))
        if self.phone:
            query = query.where(Person.phone.ilike(f"%{self.phone}%"))
        return query
