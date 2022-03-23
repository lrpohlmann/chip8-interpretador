from functools import partial
from typing import Callable
from chip8.nucleo.dados.tipos import INSTRUCAO_COMPLETA_CHIP8


def decode_8XY3(instrucao: INSTRUCAO_COMPLETA_CHIP8, func: Callable):
    vx = instrucao[1]
    vy = instrucao[2]
    return partial(func, vx, vy)
