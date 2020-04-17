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

class LandHistory(ChoiceEnum):
    SOLD = 'Vendida'
    PRIMORDIAL = 'Primordial'
    VACANT = 'Devoluta'
    AFORADA = 'Aforada' ##procurar tradução melhor para aforada 

class RequestType(ChoiceEnum):
    CONCESSION = 'Concessão'
    REQUEST = 'Requisição'
    CONFIRMATION = 'Confirmação'

class Titles(ChoiceEnum):
    CAPITAOMOR = 'CAPITAO-MOR'
    GORVERNADOR = 'GORVERNADOR'
    GORVERNADORGERAL = 'GORVERNADOR GERAL'
    CAPITAO = 'CAPITAO'
    VICEREI = 'VICE REI'
    CAMARA = 'CÂMARA'
    TRIUNVIRATO = 'TRIUNVIRATO'
    PRESIDENTEPROVINCIAL = 'PRESIDENTE PROVINCIAL'
    CAPITAOLOCOTENENTE = 'CAPITAO LOCO TENENTE'
    