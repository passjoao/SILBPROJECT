from collections import namedtuple
from enum import Enum

choice = namedtuple('Choice', 'name value')


class ChoiceEnum(Enum):
    @classmethod
    def choices(cls):
        return [choice(e.name, e.value) for e in cls]


class Gender(ChoiceEnum):
    MALE = 'MALE'
    FEMALE = 'FEMALE'
    NA = 'NA'


class LandRecordType(ChoiceEnum):
    FARM = 'FARM'
    MINING = 'MINING'
