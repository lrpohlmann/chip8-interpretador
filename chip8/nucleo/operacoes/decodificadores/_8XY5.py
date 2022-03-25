from functools import partial
from typing import Callable
from chip8.nucleo.dados.tipos import INSTRUCAO_COMPLETA_CHIP8
from chip8.nucleo.operacoes.decodificadores.subdecodificadores.padrao_XY_ import padrao_xy_


def decode_8XY5(instrucao: INSTRUCAO_COMPLETA_CHIP8, func: Callable):
    vx, vy = padrao_xy_(instrucao)
    return partial(func, vx, vy)
