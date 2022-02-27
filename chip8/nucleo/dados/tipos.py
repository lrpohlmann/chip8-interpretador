from collections import namedtuple
from typing import Any, Dict, List, Literal, Mapping, MutableMapping, Optional, Sequence, Tuple, TypeVar, Union, NewType
from typing_extensions import TypeGuard

from chip8.servicos.hexadecimais.algarismo import SEQUENCIA_ALGARISMOS_HEXADECIMAIS
from immutables import Map

DIGITOS_HEXADECIMAIS = Literal["0", "1", "2", "3", "4",
                               "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
RAM = NewType("RAM", Mapping[str, Optional[str]])
REGISTRADORES = TypeVar(
    "REGISTRADORES", MutableMapping[str, Union[str, None]], Dict[str, Union[str, None]])
REGISTRADOR_INDEX = TypeVar(
    "REGISTRADOR_INDEX", MutableMapping[Literal["i"], Union[str, None]], Dict[Literal["i"], Union[str, None]])
CONTADOR = NewType("CONTADOR", str)
INSTRUCOES_CHIP8 = TypeVar(
    "INSTRUCOES_CHIP8", Sequence[str], List[str])
SPRITE = Sequence[str]
PIXEL_MAP_COORDENADA_X = NewType("PIXEL_MAP_COORDENADA_X", int)
PIXEL_MAP_COORDENADA_Y = NewType("PIXEL_MAP_COORDENADA_Y", int)
PIXEL_MAP = TypeVar("PIXEL_MAP", MutableMapping[Tuple[PIXEL_MAP_COORDENADA_X, PIXEL_MAP_COORDENADA_Y], Literal[0, 1]], Dict[Tuple[
    PIXEL_MAP_COORDENADA_X, PIXEL_MAP_COORDENADA_Y], Literal[0, 1]])

CONTEXTO_RUNTIME_KEYS = Literal["ram", "registradores",
                                "registrador_index", "contador", "pixel_map"]
CONTEXTO_RUNTIME = Map[CONTEXTO_RUNTIME_KEYS,
                       Union[RAM, REGISTRADORES, REGISTRADOR_INDEX, CONTADOR, PIXEL_MAP]]


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
    return isinstance(obj, str)


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
