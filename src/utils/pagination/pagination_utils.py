from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import Select
from typing import Any, Dict


async def paginate_query(
    db: AsyncSession,
    query: Select,
    page: int,
    page_size: int = 10
) -> Dict[str, Any]:
    total_query = select(func.count()).select_from(query.subquery())
    total = await db.scalar(total_query)

    result = await db.execute(
        query.offset((page - 1) * page_size).limit(page_size)
    )
    rows = result.scalars().all()

    return {
        "count": total,
        "rows": rows
    }