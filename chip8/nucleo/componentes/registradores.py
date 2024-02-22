from typing import Literal


ENDERECO_REGISTRADORES = Literal[
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
]
REGISTRADORES_MAP = dict[ENDERECO_REGISTRADORES, str | None]


class Registradores:
    def __init__(
        self, inicial: REGISTRADORES_MAP | None = None, index_inicial: str | None = None
    ) -> None:
        self._reg: REGISTRADORES_MAP = {
            "0": None,
            "1": None,
            "2": None,
            "3": None,
            "4": None,
            "5": None,
            "6": None,
            "7": None,
            "8": None,
            "9": None,
            "a": None,
            "b": None,
            "c": None,
            "d": None,
            "e": None,
            "f": None,
        }

        if inicial:
            self._reg.update(inicial)

        self.i = index_inicial

    def __getitem__(self, __key: ENDERECO_REGISTRADORES) -> str:
        if __key not in self._reg.keys():
            raise Exception(f"Registradores: endereço {__key} desconhecido.")

        valor = self._reg[__key]
        if valor is None:
            raise Exception(f"Registradores: endereço {__key} vazio")

        return valor

    def __setitem__(self, __key: ENDERECO_REGISTRADORES, __value: str):
        if __key not in self._reg.keys():
            raise Exception(f"Registradores: endereço {__key} desconhecido.")

        self._reg[__key] = __value

    def __str__(self) -> str:
        return self._reg.__str__()

    def __repr__(self) -> str:
        return self._reg.__repr__()
