from typing import Any, Dict, Literal

from chip8.nucleo.dados.type_alias import REGISTRADOR_INDEX, REGISTRADORES
from chip8.servicos.inteiros.conversao import inteiros_para_hexadecimais


def criar_registradores(tamanho: int = 16) -> REGISTRADORES:
    return dict(
        [(inteiros_para_hexadecimais(endereco), None)
         for endereco in range(0, tamanho)]
    )


def criar_registrador_index() -> REGISTRADOR_INDEX:
    return {"i": None}
