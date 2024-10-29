from datetime import datetime
from enum import Enum

from beanie import Document
from pydantic import BaseModel


class Date(BaseModel):
    create_date: datetime = datetime.now()
    update_date: datetime = datetime.now()


class Active(BaseModel):
    active: bool = True


class SuperEnum(Enum):
    @classmethod
    def values(cls):
        return [e.value for e in cls]


class Language(SuperEnum):
    english = "eng"
    spanish = "es"
    japanese = "jp"


class PartOfSpeech(SuperEnum):
    verb = "verb"  # czasownik
    noun = "noun"  # rzeczownik
    adjective = "adjective"  # przymiotnik
    advers = "advers"  # przyslowek
    preposition = "preposition"  # przyimek
    conjuciton = "conjuciton"  # koniunkcja
    interjection = "interjection"  # wykrzyknik


class Word(Document, Date, Active ):
    value: str
    meaning: str
    is_learned: bool
    language: Language
    part_of_speech: PartOfSpeech


# get languages
# Language.values()

# get all active language that exists,

# get part_of_speeches

# get word with filters is_learned:bool = False, language: Language =  Language.spanish, part_of_speach: Optional[PartOfSpeaches], limit: int, offset: int, start_date, end_date

# filter alfabetic, Recently, search: str

# post add word, value, meaning, is_learend: bool = False, anguage: Language =  Language.spanish, part_of_speach: Optional[PartOfSpeaches], date : today.now()
# def add_word(value: str, meaning: str, is_learned: bool)
# put edit word, value, meaning, is_learnd: bool = False, anguage: Language =  Language.spanish, part_of_speach: Optional[PartOfSpeaches], date : today.now()

# delete delete word, word_id

# class Task(Document, Date, Active):
#     name: str

#     description: Optional[str] = None
#     priority: Optional[PriorityType] = None
#     size: Optional[SizeType] = None
#     status: StatusType = StatusType.BACKLOG
#     user: Link[User]
