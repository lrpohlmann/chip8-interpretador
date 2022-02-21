from ast import Dict
from functools import partial
from typing import Callable

from chip8.nucleo.operacoes.type_alias import RETORNO_FUNCOES_EXECUCAO


def decoder_1NNN(instrucao: str, jumpfunc: Callable[[str, Dict, Dict, str], RETORNO_FUNCOES_EXECUCAO]):
    """Decodifica a instrução 1NNN - 'jump' e repassa para um partial que executará a instrução futuramente. 
    Separa o um endereço (NNN) que será utilizado pela partial.

    Args:
        instrucao (str): Instrução completa em formato string.
        jumpfunc (Callable[[str, Dict, Dict, str], RETORNO_FUNCOES_EXECUCAO]): função que receberá o endereço num partial e executará o 'jump' posteriormente.

    Returns:
        _type_: Partial
    """
    endereco_ram_para_pular = instrucao[1:]
    return partial(jumpfunc, endereco_ram_para_pular)
