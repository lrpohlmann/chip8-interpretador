from typing import Any, Dict, Literal, MutableMapping, Sequence, TypeVar, Union

DIGITOS_HEXADECIMAIS = Literal["0", "1", "2", "3", "4",
                               "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
RAM = TypeVar(
    "RAM", MutableMapping[str, Union[str, None]], Dict[str, Union[str, None]])
REGISTRADORES = TypeVar(
    "REGISTRADORES", MutableMapping[str, Union[str, None]], Dict[str, Union[str, None]])
REGISTRADOR_INDEX = TypeVar(
    "REGISTRADOR_INDEX", MutableMapping[Literal["i"], Union[str, None]], Dict[Literal["i"], Union[str, None]])
