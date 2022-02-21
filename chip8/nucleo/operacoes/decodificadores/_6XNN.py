from typing import Callable, Dict
from functools import partial

from chip8.nucleo.operacoes.type_alias import RETORNO_FUNCOES_EXECUCAO


def decoder_6XNN(instrucao: str, func: Callable[[str, str, Dict, Dict, str], RETORNO_FUNCOES_EXECUCAO]):
    """Decodifica a instrução 6XNN - 'Set VX Register'.
    Separa o endereço do registrador (X) e o dado a ser escrito nele (NN). 
    Fornece ambos a um partial conjuntamente com a função de execucação.

    Args:
        instrucao (str): instrução em formato string
        func (Callable[[str, str, Dict, Dict, str], RETORNO_FUNCOES_EXECUCAO]): função de execução da instrução.

    Returns:
        _type_: partial
    """
    endereco_registrador = instrucao[1]
    dado = instrucao[2:]
    return partial(func, endereco_registrador, dado)
