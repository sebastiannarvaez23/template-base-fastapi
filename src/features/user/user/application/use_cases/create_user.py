from features.user.user.domain.entities.user import User
from features.user.user.adapters.repository.user_repository_impl import UserRepositoryImpl
from features.user.user.schemas.user_schema import UserCreateSchema


class CreateUser:
    def __init__(self, user_repository: UserRepositoryImpl):
        self.user_repository = user_repository

    async def execute(self, user_data: UserCreateSchema) -> User:
        user_dict = user_data.dict()
        return self.user_repository.create(user_dict)