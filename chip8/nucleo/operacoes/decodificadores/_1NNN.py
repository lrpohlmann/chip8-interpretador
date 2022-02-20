from ast import Dict
from typing import Callable
from functools import partial

from chip8.nucleo.operacoes.type_alias import RETORNO_FUNCOES_EXECUCAO


def decoder_1NNN(instrucao: str, jumpfunc: Callable[[str, Dict, Dict, str], RETORNO_FUNCOES_EXECUCAO]):
    endereco_ram_para_pular = instrucao[1:]
    return partial(jumpfunc, endereco_ram_para_pular)
