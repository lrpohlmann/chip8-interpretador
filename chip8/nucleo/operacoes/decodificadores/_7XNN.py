from functools import partial
from typing import Callable

from chip8.nucleo.operacoes.type_alias import RETORNO_FUNCOES_EXECUCAO
from chip8.nucleo.dados.type_alias import RAM, REGISTRADORES


def decoder_7XNN(instrucao: str, func: Callable[[str, str, RAM, REGISTRADORES, str], RETORNO_FUNCOES_EXECUCAO]):
    """Decodifica a instrução 7XNN - 'Add value to Register VX'.
    Separa o endereço do registrador (X) e o valor a adicionar (NN). Fornece ambos e a função de execução da instrução para um partial.

    Args:
        instrucao (str): instrução em formato string.
        func (Callable[[str, str, RAM, REGISTRADORES, str], RETORNO_FUNCOES_EXECUCAO]): função de execução.

    Returns:
        Partial: callable pronto para futura execução da instrução.
    """
    endereco_registrador = instrucao[1]
    dado = instrucao[2:]
    return partial(func, endereco_registrador, dado)
