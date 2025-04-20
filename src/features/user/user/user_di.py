from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from config.session import get_db
from features.user.user.adapters.repository.user_repository_impl import UserRepositoryImpl


def get_user_repository(db: AsyncSession = Depends(get_db)) -> UserRepositoryImpl:
    return UserRepositoryImpl(db)

# uses cases

def get_get_users_use_case(
    user_repository: UserRepositoryImpl = Depends(get_user_repository)
) -> GetUsers:
    return GetUsers(user_repository)

def get_get_user_by_id_use_case(
    user_repository: UserRepositoryImpl = Depends(get_user_repository)
) -> GetUserById:
    return GetUserById(user_repository)

def get_create_user_use_case(
    user_repository: UserRepositoryImpl = Depends(get_user_repository)
) -> CreateUser:
    return CreateUser(user_repository)


def get_update_user_use_case(
    user_repository: UserRepositoryImpl = Depends(get_user_repository)
) -> UpdateUser:
    return UpdateUser(user_repository)

# ---

def get_user_service(
    create_user_use_case: CreateUser = Depends(get_create_user_use_case),
    get_user_by_id_use_case: GetUserById = Depends(get_get_user_by_id_use_case),
    get_users_use_case: GetUsers = Depends(get_get_users_use_case),
    update_user_use_case: UpdateUser = Depends(get_update_user_use_case),
):
    from features.user.user.application.services.user_service import UserService
    return UserService(
        get_users_use_case=get_users_use_case,
        get_user_by_id_use_case=get_user_by_id_use_case,
        create_user_use_case=create_user_use_case,
        update_user_use_case=update_user_use_case,
    )