from typing import Callable, Dict, Tuple

from chip8.nucleo.dados.type_alias import RAM, REGISTRADORES, REGISTRADOR_INDEX

RETORNO_FUNCOES_EXECUCAO = Tuple[RAM, REGISTRADORES, REGISTRADOR_INDEX, str]
FUNCOES_EXECUCAO = Callable[[RAM, REGISTRADORES,
                             REGISTRADOR_INDEX, str], RETORNO_FUNCOES_EXECUCAO]
