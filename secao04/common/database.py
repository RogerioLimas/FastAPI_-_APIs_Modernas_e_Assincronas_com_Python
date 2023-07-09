from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, AsyncSession
from common.configs import settings


engine: AsyncEngine = create_async_engine(settings.DATABASE_URL)
Session: AsyncSession = sessionmaker(
    autoflush=False,
    expire_on_commit=False,
    class_=AsyncSession,
    bind=engine
)
