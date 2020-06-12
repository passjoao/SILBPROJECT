from collections import namedtuple
from enum import Enum

choice = namedtuple('Choice', 'name value')


class ChoiceEnum(Enum):
    @classmethod
    def choices(cls):
        return [choice(e.name, e.value) for e in cls]


class Gender(ChoiceEnum):
    MALE = 'Homem'
    FEMALE = 'Mulher'
    NA = 'NA'


class MatrialStatus(ChoiceEnum):
    CASADO = 'Casado'
    SOLTEIRO = 'Solteiro'
    DIVORCIADO = 'Divorciado'
    VIUVO = 'Viúvo'


class LandRecordType(ChoiceEnum):
    FARM = 'Fazenda'
    MINING = 'Mineração'


class LandHistory(ChoiceEnum):
    SOLD = 'Comprada'
    PRIMORDIAL = 'Primordial'
    HERDED = 'Herdada'
    VACANT = 'Devoluta nunca povoada'
    ABANDONED = 'Devoluta por abandono'
    RENTED = 'Aforada'  ##procurar tradução melhor para aforada


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
