from functools import partial
from typing import Callable
from chip8.nucleo.dados.type_alias import RAM, REGISTRADOR_INDEX, REGISTRADORES
from chip8.nucleo.operacoes.type_alias import FUNCOES_EXECUCAO, RETORNO_FUNCOES_EXECUCAO


def decoder_ANNN(instrucao: str, func: Callable[[str, RAM, REGISTRADORES, REGISTRADOR_INDEX, str], RETORNO_FUNCOES_EXECUCAO]):
    """Decodifica a instrução ANNN - 'set index register'.
    Obtém o dado (NNN) e o fornece para um partial conjuntamente com a função de execução da instrução.

    Args:
        instrucao (str): instrução em formato string.
        func (Callable[[str, RAM, REGISTRADORES, REGISTRADOR_INDEX, str], RETORNO_FUNCOES_EXECUCAO]): função de execução da instrução.

    Returns:
        Partial: callable pronto para futura execução da instrução.
    """
    endereco = instrucao[1:]
    return partial(func, endereco)
