from typing import Optional

from beanie import PydanticObjectId
from bson import ObjectId
from pymongo import ASCENDING, DESCENDING

from app.models import Language, PartOfSpeech, SortBy, Word


async def get_words(
    sort_by: SortBy,
    text: Optional[str] = None,
    is_learned: Optional[bool] = None,
    language: Optional[Language] = None,
    part_of_speech: Optional[PartOfSpeech] = None,
) -> list[Word]:
    search_criteria = {}
    if isinstance(is_learned, bool):
        search_criteria["is_learned"] = is_learned
    if text is not None:
        ilike = {"$regex": text, "$options": "i"}
        search_criteria["$or"] = [{"value": ilike}, {"meaning": ilike}]
        # search_criteria["value"] = Regex(pattern=value, flags="i")
    if language is not None:
        search_criteria["language"] = language
    if part_of_speech is not None:
        search_criteria["part_of_speech"] = part_of_speech
    if sort_by == SortBy.recently:
        sort_by = (Word.create_date, DESCENDING)
    else:
        sort_by = (Word.value, ASCENDING)
    return await Word.find(search_criteria).sort(sort_by).to_list()


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
    print(id, value, is_learned, language, part_of_speech)
    # word = await Word.find_one(Word.id == id)  # TODO: why it's not working
    word = await Word.get(document_id=id)
    print(word.model_dump())
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


async def get_word(
    id: str,
) -> Word:
    return await Word.get(document_id=PydanticObjectId(ObjectId(id)))
