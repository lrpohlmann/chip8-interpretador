from typing import Callable, Dict
from functools import partial

from chip8.nucleo.operacoes.type_alias import RETORNO_FUNCOES_EXECUCAO


def decoder_6XNN(instrucao, func: Callable[[str, str, Dict, Dict, str], RETORNO_FUNCOES_EXECUCAO]):
    endereco_registrador = instrucao[1]
    dado = instrucao[2:]
    return partial(func, endereco_registrador, dado)
