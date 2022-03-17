from functools import partial
from typing import Any, Callable
from chip8.nucleo.dados.tipos import CONTEXTO_RUNTIME, FUNCOES_EXECUCAO, INSTRUCAO_COMPLETA_CHIP8


def decoder_8XY0(instrucao: INSTRUCAO_COMPLETA_CHIP8, func: Callable):
    endereco_registrador_x = instrucao[1]
    endereco_registrador_y = instrucao[2]
    return partial(func, endereco_registrador_x, endereco_registrador_y)
