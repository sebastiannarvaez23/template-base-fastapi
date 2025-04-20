from fastapi import APIRouter, Depends, Query

from uuid import UUID

from core.schemas.paginated_response import PaginatedResponse
from features.user.user.application.services.user_service import UserService
from features.user.user.user_di import get_user_service
from features.user.user.schemas.user_schema import (
    UserCreateSchema,
    UserUpdateSchema,
    UserResponseSchema,
    UserFilterSchema
)


userRouter = APIRouter()

@userRouter.get("/user", response_model=PaginatedResponse[UserResponseSchema])
async def get_users(
    page: int = Query(..., ge=1),
    filters: UserFilterSchema = Depends(),
    user_service: UserService = Depends(get_user_service)
):
    return await user_service.get_users(page, filters)

@userRouter.get("/user/{user_id}", response_model=UserResponseSchema)
async def get_user_by_id(
    user_id: UUID,
    user_service: UserService = Depends(get_user_service)
):
    return await user_service.get_user_by_id(user_id)

@userRouter.get("/user/{nickname}", response_model=UserResponseSchema)
async def get_user_by_id(
    nickname: str,
    user_service: UserService = Depends(get_user_service)
):
    return await user_service.get_user_by_nickname(nickname)

@userRouter.post("/user", response_model=UserResponseSchema)
async def create_user(
    user_data: UserCreateSchema,
    user_service: UserService = Depends(get_user_service),
):
    return await user_service.create_user(user_data)


@userRouter.put("/user/{user_id}", response_model=UserResponseSchema)
async def update_user(
    user_id: UUID,
    user_data: UserUpdateSchema,
    user_service: UserService = Depends(get_user_service)
):
    return await user_service.update_user(user_id, user_data)