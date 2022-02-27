from functools import partial
from typing import Callable

from chip8.nucleo.dados.tipos import PIXEL_MAP, RAM, REGISTRADOR_INDEX, REGISTRADORES, CONTEXTO_RUNTIME


def decoder_DXYN(instrucao: str, func: Callable[[str, str, str, RAM, REGISTRADORES, REGISTRADOR_INDEX, str, PIXEL_MAP], CONTEXTO_RUNTIME]):
    """Decodifica a instrução DXYN - 'draw a sprite on screen'.
    Obtém os dados do VX (X) e do VY (Y) que serão as coordenadas 'x' e 'y' da tela; 
    Obtém o número de bytes para ler a partir do endereço registrado no registrador index e formar o sprite.

    Args:
        instrucao (str): instrução em formato string.
        func (Callable[[str, str, str, RAM, REGISTRADORES, REGISTRADOR_INDEX, str], CONTEXTO_RUNTIME]): função de execução da instrução.

    Returns:
        Partial: callable pronto para futura execução da instrução.
    """
    vx = instrucao[1]
    vy = instrucao[2]
    bytes_para_ler = instrucao[3]
    return partial(func, vx, vy, bytes_para_ler)
