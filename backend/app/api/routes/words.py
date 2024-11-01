from http.client import HTTPException
from typing import Any

from fastapi import APIRouter

from app.crud import add_word, get_word, get_words, remove_word, update_word
from app.models import Language, PartOfSpeech, Word, WordCreate, SortBy

router = APIRouter()


@router.get("/")
async def read_words(
    text: str | None = None,
    is_learned: bool | None = None,
    language: Language | None = None,
    part_of_speech: PartOfSpeech | None = None,
    sort_by: SortBy = SortBy.recently,
) -> Any:
    return await get_words(
        text=text,
        is_learned=is_learned,
        language=language,
        part_of_speech=part_of_speech,
        sort_by=sort_by,
    )


@router.post("/", response_model=Word)
async def create_word(*, new_word: WordCreate) -> Any:  # TODO: why we use *
    return await add_word(**new_word.model_dump())


@router.get("/{id}")
async def read_word(id: str) -> Any:
    word = await get_word(id=id)
    if not word:
        raise HTTPException(status_code=404, detail="Item not found")
    return word


@router.delete("/{id}")
async def delete(id: str) -> Any:
    return await remove_word(id=id)


@router.post("/{id}", response_model=Word)
async def update(id: str, word: WordCreate) -> Any:
    return await update_word(id=id, **word.model_dump())
