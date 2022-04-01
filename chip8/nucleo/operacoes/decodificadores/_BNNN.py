from functools import partial
from typing import Callable
from chip8.nucleo.dados.tipos import INSTRUCAO_COMPLETA_CHIP8
from chip8.nucleo.operacoes.decodificadores.subdecodificadores.padrao_NNN import padrao_NNN


def decode_BNNN(instrucao: INSTRUCAO_COMPLETA_CHIP8, func: Callable):
    endereco_para_pular = padrao_NNN(instrucao)
    return partial(func, endereco_para_pular)
