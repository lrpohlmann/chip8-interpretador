from collections import namedtuple
from typing import Any, Callable, Dict, List, Literal, Mapping, MutableMapping, Optional, Sequence, Tuple, TypeVar, Union, NewType
from typing_extensions import TypeGuard

from chip8.servicos.hexadecimais.algarismo import SEQUENCIA_ALGARISMOS_HEXADECIMAIS
from immutables import Map

DIGITOS_HEXADECIMAIS = Literal["0", "1", "2", "3", "4",
                               "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
RAM = NewType("RAM", Map[str, Optional[str]])
REGISTRADORES = NewType("REGISTRADORES", Map[str, Optional[str]])
REGISTRADOR_INDEX = NewType(
    "REGISTRADOR_INDEX", Map[Literal["i"], Optional[str]])
CONTADOR = NewType("CONTADOR", str)
INSTRUCAO_COMPLETA_CHIP8 = NewType("INSTRUCAO_COMPLETA_CHIP8", str)
SEQUENCIA_INSTRUCOES_CHIP8_FRACIONADAS_EM_2BYTES = TypeVar(
    "SEQUENCIA_INSTRUCOES_CHIP8_FRACIONADAS_EM_2BYTES", Sequence[str], List[str])
SPRITE = Sequence[str]
PIXEL_MAP_COORDENADA_X = NewType("PIXEL_MAP_COORDENADA_X", int)
PIXEL_MAP_COORDENADA_Y = NewType("PIXEL_MAP_COORDENADA_Y", int)
PIXEL_MAP = NewType(
    "PIXEL_MAP", Map[Tuple[PIXEL_MAP_COORDENADA_X, PIXEL_MAP_COORDENADA_Y], Literal[0, 1]])

R = TypeVar("R")
FUNCOES_EXECUCAO = Callable[[R], R]

CONTEXTO_RUNTIME_KEYS = Literal["ram", "registradores",
                                "registrador_index", "contador", "pixel_map", "ultima_instrucao", "ultima_execucao"]
CONTEXTO_RUNTIME = Map[CONTEXTO_RUNTIME_KEYS,
                       Union[RAM, REGISTRADORES, REGISTRADOR_INDEX, CONTADOR, PIXEL_MAP, INSTRUCAO_COMPLETA_CHIP8, FUNCOES_EXECUCAO]]


def e_instrucao(obj: Any) -> TypeGuard[INSTRUCAO_COMPLETA_CHIP8]:
    return all([isinstance(obj, str), len(obj) == 4, all(
        [(digito in SEQUENCIA_ALGARISMOS_HEXADECIMAIS) for digito in obj])])


def e_ram(obj: Any) -> TypeGuard[RAM]:
    valores = all(
        [
            (val == None or type(val) == str) for val in obj.values()
        ]
    )
    keys = all(
        [
            (type(val) == str) for val in obj.keys()
        ]
    )

    return all([keys, valores])


def e_registrador(obj: Any) -> TypeGuard[REGISTRADORES]:
    valores = all(
        [
            (val == None or isinstance(val, str)) for val in obj.values()
        ]
    )

    keys = all(
        [
            val in SEQUENCIA_ALGARISMOS_HEXADECIMAIS for val in obj.keys()
        ]
    )

    return all([keys, valores])


def e_registrador_index(obj: Any) -> TypeGuard[REGISTRADOR_INDEX]:
    keys = (len(obj.keys()) == 1 and list(obj.keys())[0] == "i")

    valores = (isinstance(obj["i"], str) or obj["i"] == None)

    return all([keys, valores])


def e_contador(obj: Any) -> TypeGuard[CONTADOR]:
    return all([isinstance(obj, str), all(
        [(digito in SEQUENCIA_ALGARISMOS_HEXADECIMAIS) for digito in obj])])


def e_pixel_map(obj: Any) -> TypeGuard[PIXEL_MAP]:
    valores = all(
        [
            isinstance(val, int) for val in obj.values()
        ]
    )

    keys = all(
        [
            isinstance(val, tuple) for val in obj.keys()
        ]
    )

    return all([keys, valores])
