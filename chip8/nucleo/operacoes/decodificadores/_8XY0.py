from functools import partial
from typing import Any, Callable
from chip8.nucleo.dados.tipos import CONTEXTO_RUNTIME, FUNCOES_EXECUCAO, INSTRUCAO_COMPLETA_CHIP8
from chip8.nucleo.operacoes.decodificadores.subdecodificadores.padrao_XY_ import padrao_xy_


def decoder_8XY0(instrucao: INSTRUCAO_COMPLETA_CHIP8, func: Callable):
    vx, vy = padrao_xy_(instrucao)
    return partial(func, vx, vy)
