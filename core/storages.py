import redis.asyncio
from faststream.redis.fastapi import RedisBroker, RedisRouter
from redis.asyncio import Redis
from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine

from core import config


class Database:
    def __init__(self):
        self.engine = create_async_engine(config.settings.PG_DSN, echo=True)

    async def init(self, metadata: MetaData):
        async with self.engine.connect() as connection:
            # await connection.run_sync(metadata.drop_all)
            await connection.run_sync(metadata.create_all)
            await connection.commit()
        await self.engine.dispose()

    async def dispose(self):
        await self.engine.dispose()

    def __call__(self) -> AsyncEngine:
        return self.engine


class RedisStorage:

    def __init__(self,
                 dsn: str):
        self._pool: redis.asyncio.ConnectionPool = redis.asyncio.ConnectionPool.from_url(
            dsn
        )
        self.connection: Redis = Redis(connection_pool=self._pool, decode_responses=True)

    async def __aenter__(self):
        self.connection = Redis(connection_pool=self._pool)
        return self.connection

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.connection.close()

    async def __call__(self):
        return self




session_storage = RedisStorage(config.settings.SESSION_STORAGE_URI)