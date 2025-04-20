from utils.pagination.pagination_utils import paginate_query

from features.user.person.adapters.repository.person_repository_impl import PersonRepositoryImpl
from features.user.person.domain.utils.person_filter import PersonFilter


class GetPersons:
    def __init__(self, person_repository: PersonRepositoryImpl):
        self.person_repository = person_repository

    async def execute(self, page: int, filters: dict):
        base_query = await self.person_repository.query()
        query = PersonFilter(**filters.dict()).apply(base_query)
        return await paginate_query(self.person_repository.db, query, page)