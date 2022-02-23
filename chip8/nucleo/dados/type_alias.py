from collections import namedtuple
from typing import Any, Dict, List, Literal, Mapping, MutableMapping, Sequence, Tuple, TypeVar, Union, NewType

DIGITOS_HEXADECIMAIS = Literal["0", "1", "2", "3", "4",
                               "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
RAM = TypeVar(
    "RAM", MutableMapping[str, Union[str, None]], Dict[str, Union[str, None]])
REGISTRADORES = TypeVar(
    "REGISTRADORES", MutableMapping[str, Union[str, None]], Dict[str, Union[str, None]])
REGISTRADOR_INDEX = TypeVar(
    "REGISTRADOR_INDEX", MutableMapping[Literal["i"], Union[str, None]], Dict[Literal["i"], Union[str, None]])
INSTRUCOES_CHIP8 = TypeVar(
    "INSTRUCOES_CHIP8", Sequence[str], List[str])
SPRITE = Sequence[str]
PIXEL_MAP_COORDENADA_X = NewType("PIXEL_MAP_COORDENADA_X", int)
PIXEL_MAP_COORDENADA_Y = NewType("PIXEL_MAP_COORDENADA_Y", int)
PIXEL_MAP = TypeVar("PIXEL_MAP", MutableMapping[Tuple[PIXEL_MAP_COORDENADA_X, PIXEL_MAP_COORDENADA_Y], Literal[0, 1]], Dict[Tuple[
    PIXEL_MAP_COORDENADA_X, PIXEL_MAP_COORDENADA_Y], Literal[0, 1]])
