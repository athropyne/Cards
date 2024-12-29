from contextlib import asynccontextmanager

from starlette.middleware.cors import CORSMiddleware

from core import storages

from fastapi import FastAPI

from core.schemas import metadata
from core.storages import Database
from services.security.routes import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    database = Database()
    await database.init(metadata)
    await storages.session_storage.connection.info()
    yield
    await database.dispose()
    await storages.session_storage.connection.aclose(close_connection_pool=True)


app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)


