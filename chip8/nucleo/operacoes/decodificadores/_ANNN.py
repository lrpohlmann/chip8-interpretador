from functools import partial
from chip8.nucleo.operacoes.type_alias import FUNCOES_EXECUCAO


def decoder_ANNN(instrucao, func) -> FUNCOES_EXECUCAO:
    endereco = instrucao[1:]
    return partial(func, endereco)
