from typing import Dict
from sqlalchemy.sql import Select
from utils.pagination.pagination_utils import paginate_query

from features.user.user.adapters.repository.user_repository_impl import UserRepositoryImpl
from features.user.user.domain.utils.user_filter import UserFilter


class GetUsers:
    def __init__(self, person_repository: UserRepositoryImpl):
        self.person_repository = person_repository

    async def execute(self, page: int, filters: dict):
        base_query = await self.person_repository.query()
        query = UserFilter(**filters.dict()).apply(base_query)
        return await paginate_query(self.person_repository.db, query, page)