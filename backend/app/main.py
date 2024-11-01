from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.routing import APIRoute
from starlette.middleware.cors import CORSMiddleware

from app.api.main import api_router
from app.core.config import settings
# from backend.app.database_connection import database_init
# from backend.app.models import Word

import os

from beanie import Document, init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from app.database_connection import database_init
# def custom_generate_unique_id(route: APIRoute) -> str:
# return f"{route.tags[0]}-{route.name}"


@asynccontextmanager
async def lifespan(app: FastAPI):
    await database_init()
    app.include_router(api_router)
    yield
    # Clean up the ML models and release the resources


app = FastAPI(
    title=settings.PROJECT_NAME,
    lifespan=lifespan,
    # openapi_url=f"{settings.API_V1_STR}/openapi.json",
    # generate_unique_id_function=custom_generate_unique_id,
)

# Set all CORS enabled origins
if settings.all_cors_origins:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.all_cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
