from functools import partial
from typing import Callable, Dict

from chip8.nucleo.operacoes.type_alias import RETORNO_FUNCOES_EXECUCAO
from chip8.nucleo.dados.type_alias import RAM, REGISTRADORES


def decoder_7XNN(instrucao: str, func: Callable[[str, str, RAM, REGISTRADORES, str], RETORNO_FUNCOES_EXECUCAO]):
    endereco_registrador = instrucao[1]
    dado = instrucao[2:]
    return partial(func, endereco_registrador, dado)
