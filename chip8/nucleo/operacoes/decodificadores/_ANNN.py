from functools import partial
from typing import Callable
from chip8.nucleo.dados.type_alias import PIXEL_MAP, RAM, REGISTRADOR_INDEX, REGISTRADORES
from chip8.nucleo.operacoes.type_alias import FUNCOES_EXECUCAO, CONTEXTO_RUNTIME


def decoder_ANNN(instrucao: str, func: Callable[[str, RAM, REGISTRADORES, REGISTRADOR_INDEX, str, PIXEL_MAP], CONTEXTO_RUNTIME]):
    """Decodifica a instrução ANNN - 'set index register'.
    Obtém o dado (NNN) e o fornece para um partial conjuntamente com a função de execução da instrução.

    Args:
        instrucao (str): instrução em formato string.
        func (Callable[[str, RAM, REGISTRADORES, REGISTRADOR_INDEX, str], CONTEXTO_RUNTIME]): função de execução da instrução.

    Returns:
        Partial: callable pronto para futura execução da instrução.
    """
    endereco = instrucao[1:]
    return partial(func, endereco)
