from functools import partial
from typing import Callable
from chip8.nucleo.dados.tipos import INSTRUCAO_COMPLETA_CHIP8


def decoder_8XY2(instrucao: INSTRUCAO_COMPLETA_CHIP8, func: Callable):
    vx = instrucao[1]
    vy = instrucao[2]
    return partial(func, vx, vy)
