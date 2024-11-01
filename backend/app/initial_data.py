from asyncio import run

from app.crud import add_word, get_word, get_words, remove_word, update_word
from app.database_connection import database_init
from app.models import Language, PartOfSpeech, Word


async def init():
    await database_init(document_models=[Word], clean_database=True)
    words = [
        Word(
            value="amigo",
            meaning="friend",
            is_learned=True,
            language=Language.spanish,
            part_of_speech=PartOfSpeech.noun,
        ),
        Word(
            value="hablar",
            meaning="talk",
            is_learned=True,
            language=Language.spanish,
            part_of_speech=PartOfSpeech.verb,
        ),
        Word(
            value="hacer",
            meaning="do",
            is_learned=False,
            language=Language.spanish,
            part_of_speech=PartOfSpeech.verb,
        ),
    ]
    await Word.insert_many(words)

    words = await get_words(is_learned=False)
    assert len(words) == 1

    words = await get_words(part_of_speech=PartOfSpeech.noun)
    assert len(words) == 1

    words = await get_words()
    assert len(words) == 3

    words = await get_words(value="ami")
    assert len(words) == 1

    word = await add_word(
        value="correr",
        meaning="run",
        is_learned=True,
        language=Language.spanish,
        part_of_speech=PartOfSpeech.verb,
    )

    words = await get_words()
    assert len(words) == 4

    word = await update_word(
        id=word.id,
        value="gordo",
        meaning="fat",
        is_learned=False,
        language=Language.spanish,
        part_of_speech=PartOfSpeech.adjective,
    )
    assert (
        word.value == "gordo"
        and word.meaning == "fat"
        and word.is_learned == False
        and word.part_of_speech == PartOfSpeech.adjective
    )
    word = await get_word(word.id)
    assert (
        word.value == "gordo"
        and word.meaning == "fat"
        and word.is_learned == False
        and word.part_of_speech == PartOfSpeech.adjective
    )

    await remove_word(id=word.id)
    words = await get_words()
    assert len(words) == 3


if __name__ == "__main__":
    run(init())
