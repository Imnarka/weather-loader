"""
Конфигурация подключения к БД
"""

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from config import settings

engine = create_async_engine(settings.DB_URL)
async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=True)


class Base(DeclarativeBase):
    pass
