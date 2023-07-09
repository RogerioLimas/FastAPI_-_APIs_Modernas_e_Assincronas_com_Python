from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession
from common.database import Session


async def get_session() -> AsyncGenerator:
    session: AsyncSession = Session()

    try:
        yield session
    finally:
        await session.close()
