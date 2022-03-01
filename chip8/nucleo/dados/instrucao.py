from functools import reduce
from telnetlib import SE
from typing import Union
from typing import Sequence, overload
from collections.abc import Sequence as SequenciaABC
from chip8.nucleo.dados.tipos import INSTRUCAO_COMPLETA_CHIP8, e_instrucao


def criar_instrucao(arg: Union[str, Sequence[str]]) -> INSTRUCAO_COMPLETA_CHIP8:
    instrucao = ""
    if isinstance(arg, str):
        instrucao += arg
    elif isinstance(arg, SequenciaABC):
        instrucao = reduce(lambda x, y: x+y, arg, instrucao)
    else:
        raise Exception()

    if e_instrucao(instrucao):
        return instrucao
    else:
        raise Exception(
            f"Instrução {instrucao} formada não é uma instrução Chip-8 válida.")
