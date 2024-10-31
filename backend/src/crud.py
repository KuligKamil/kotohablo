from typing import Optional

from bson import Regex
from pymongo import DESCENDING
from src.models import Language, PartOfSpeech, Word


async def add_word(
    value: str,
    meaning: str,
    is_learned: bool,
    language: Language = Language.spanish,
    part_of_speech: PartOfSpeech = PartOfSpeech.verb,
) -> Word:
    return await Word.insert(
        Word(
            value=value,
            meaning=meaning,
            is_learned=is_learned,
            language=language,
            part_of_speech=part_of_speech,
        )
    )


async def update_word(
    id: str,
    value: str,
    meaning: str,
    is_learned: bool,
    language: Language = Language.spanish,
    part_of_speech: PartOfSpeech = PartOfSpeech.verb,
) -> Word:
    word = await Word.find_one(Word.id == id)
    word.value = value
    word.meaning = meaning
    word.is_learned = is_learned
    word.language = language  # maybe not useful
    word.part_of_speech = part_of_speech
    await word.save()
    return word


async def remove_word(
    id: str,
) -> Word:
    await Word.find_one(Word.id == id).delete()


# async def get_word(
#     id: str,
# ) -> Word:
#     return await Word.find_one(Word.id == id)


async def get_words(
    value: Optional[str] = None,
    # meaning: str,
    is_learned: Optional[bool] = None,
    language: Optional[Language] = None,
    part_of_speech: Optional[PartOfSpeech] = None,
) -> list[Word]:
    search_criteria = {}
    if isinstance(is_learned, bool):
        search_criteria["is_learned"] = is_learned
    if value is not None:
        search_criteria["value"] = {"$regex": value, "$options": "i"}
        # search_criteria["value"] = Regex(pattern=value, flags="i")
    if language is not None:
        search_criteria["language"] = language
    if part_of_speech is not None:
        search_criteria["part_of_speech"] = part_of_speech
    return (
        await Word.find(search_criteria).sort((Word.create_date, DESCENDING)).to_list()
    )
