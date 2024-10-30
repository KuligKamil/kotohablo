from asyncio import run

from src.crud import get_words
from src.database_connection import database_init
from src.models import Word, Language, PartOfSpeech


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
    words_ids = await Word.insert_many(words)
    # words = await Word.find({"is_learned": True}).to_list()
    # words = await ws()
    words = await get_words(is_learned=False)
    print(len(words))
    assert len(words) == 1

    words = await get_words(part_of_speech=PartOfSpeech.noun)
    print(len(words))
    assert len(words) == 1

    words = await get_words()
    print(len(words))
    assert len(words) == 3

    words = await get_words(value="ami")
    print(len(words))
    assert len(words) == 1


if __name__ == "__main__":
    run(init())
