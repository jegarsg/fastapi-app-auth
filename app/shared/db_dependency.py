from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession
from app.infrastructure.database.session import async_session

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session
