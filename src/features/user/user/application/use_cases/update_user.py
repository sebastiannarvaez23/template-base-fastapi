from features.user.user.adapters.repository.user_repository_impl import UserRepositoryImpl
from features.user.user.domain.entities.user import User
from features.user.user.schemas.user_schema import UserUpdateSchema


class UpdateUser:
    def __init__(self, user_repository: UserRepositoryImpl):
        self.user_repository = user_repository

    async def execute(self, user: User, user_data: UserUpdateSchema) -> User:
        user_data_dict = user_data.dict(exclude_unset=True)
        return await self.user_repository.update(user, user_data_dict)