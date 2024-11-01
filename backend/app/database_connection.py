import os

from beanie import Document, init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from app.models import Word


async def database_init(clean_database: bool = False) -> None:
    client: AsyncIOMotorClient = AsyncIOMotorClient(os.getenv("MONGODB_URI"))
    await init_beanie(
        database=client.kotohablo,
        document_models=[Word],
        # multiprocessing_mode=True,
    )
    if clean_database:
        await client.drop_database(name_or_database=client.kotohablo)
