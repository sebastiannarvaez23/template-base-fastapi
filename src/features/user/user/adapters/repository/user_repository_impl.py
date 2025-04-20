from sqlalchemy.ext.asyncio import AsyncSession

from core.repository.base_repository import BaseRepository
from features.user.user.domain.entities.user import User
from features.user.user.schemas.user_schema import UserCreateSchema, UserUpdateSchema


class UserRepositoryImpl(BaseRepository[User, UserCreateSchema, UserUpdateSchema]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, User)
        
    async def get_by_nickname(self, nickname: str):
        stmt = (await self.query()).where(self.model.id == nickname)
        result = await self.db.execute(stmt)
        return result.scalar_one_or_none()