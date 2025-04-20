from typing import Optional

from features.user.user.adapters.repository.user_repository_impl import UserRepositoryImpl
from features.user.user.domain.entities.user import User


class GetUserByNickname:
    def __init__(self, user_repository: UserRepositoryImpl):
        self.user_repository = user_repository

    async def execute(self, nickname: str) -> Optional[User]:
        return await self.user_repository.get_by_nickname(nickname)