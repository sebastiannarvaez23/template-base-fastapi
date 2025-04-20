from sqlalchemy.sql import Select

from core.filters.base_query_filter import BaseFilter
from features.user.user.domain.entities.user import User

class UserFilter(BaseFilter[User]):
    def __init__(self, nickname=None, origin=None, active=None, **kwargs):
        self.nickname = nickname
        self.origin = origin
        self.active = active
        
    def apply(self, query: Select) -> Select:
        if self.nickname:
            query = query.where(User.nickname.ilike(f"%{self.nickname}%"))
        if self.origin:
            query = query.where(User.origin.ilike(f"%{self.origin}%"))
        if self.active is not None:
            query = query.where(User.active == self.active)
        return query