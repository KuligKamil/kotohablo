from http.client import HTTPException
from typing import Any

from fastapi import APIRouter

from app.crud import add_word, get_word, get_words
from app.models import Word, WordCreate

router = APIRouter()


@router.get("/")
async def read_words() -> Any:
    return await get_words()


@router.get("/{id}")
async def read_word(id: str) -> Any:
    word = await get_word(id=id)
    if not word:
        raise HTTPException(status_code=404, detail="Item not found")
    return word


@router.post("/", response_model=Word)
async def create_word(*, new_word: WordCreate) -> Any:
    print()
    return await add_word(**new_word.model_dump())
