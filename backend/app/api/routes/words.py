from typing import Any

from fastapi import APIRouter

from app.crud import get_words

router = APIRouter()


@router.get("/")
async def read_words() -> Any:
    """
    Retrieve items.
    """
    return await get_words()
    # return await Word.find().to_list()
    # return words
    # return {"Hello"}
