from functools import partial
from typing import Callable
from chip8.nucleo.dados.tipos import INSTRUCAO_COMPLETA_CHIP8


def decoder_8XY1(instrucao: INSTRUCAO_COMPLETA_CHIP8, func: Callable):
    endereco_registrador_vx = instrucao[1]
    endereco_registrador_vy = instrucao[2]
    return partial(func, endereco_registrador_vx, endereco_registrador_vy)
