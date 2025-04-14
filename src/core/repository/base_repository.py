from abc import ABC
from datetime import datetime
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import Generic, TypeVar, Type, Optional
from uuid import UUID

T = TypeVar("T")
C = TypeVar("C")
U = TypeVar("U")


class BaseRepository(ABC, Generic[T, C, U]):
    def __init__(self, db: AsyncSession, model: Type[T]):
        self.db = db
        self.model = model

    async def query(self):
        return select(self.model).where(self.model.deleted_at.is_(None))

    async def get_by_id(self, id: UUID) -> Optional[T]:
        stmt = (await self.query()).where(self.model.id == id)
        result = await self.db.execute(stmt)
        return result.scalar_one_or_none()

    async def create(self, create_data: C) -> T:
        instance = self.model(**create_data)
        self.db.add(instance)
        await self.db.commit()
        await self.db.refresh(instance)
        return instance

    async def update(self, instance: T, update_data: U) -> T:
        for field, value in update_data.dict(exclude_unset=True).items():
            setattr(instance, field, value)
        self.db.add(instance)
        await self.db.commit()
        await self.db.refresh(instance)
        return instance

    async def delete(self, instance: T) -> None:
        instance.deleted_at = datetime.utcnow()
        self.db.add(instance)
        await self.db.commit()
        return instance
