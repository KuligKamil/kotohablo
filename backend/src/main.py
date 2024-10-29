from asyncio import run

from database_connection import database_init
from models import Word, Language, PartOfSpeech


async def init():
    await database_init(document_models=[Word], clean_database=True)
    words = [
        Word(
            value="hablar",
            meaning="talk",
            is_learned=True,
            language=Language.spanish,
            part_of_speech=PartOfSpeech.verb,
        )
    ]
    words_ids = await Word.insert_many(words)


if __name__ == "__main__":
    run(init())
