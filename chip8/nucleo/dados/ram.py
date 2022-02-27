from typing import Any, Dict
from chip8.servicos.inteiros.conversao import inteiros_para_hexadecimais
from chip8.nucleo.dados.tipos import RAM


def criar_memoria_ram(tamanho: int = 4096) -> RAM:
    return dict(
        [(inteiros_para_hexadecimais(n), None) for n in range(0, tamanho)]
    )
