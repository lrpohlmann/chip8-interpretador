from typing import Callable, Dict, Literal, Mapping, Tuple, Union

from chip8.nucleo.dados.type_alias import RAM, REGISTRADORES, REGISTRADOR_INDEX, PIXEL_MAP

RETORNO_FUNCOES_EXECUCAO_KEYS = Literal["ram", "registradores",
                                        "registrador_index", "contador", "pixel_map"]
RETORNO_FUNCOES_EXECUCAO = Mapping[RETORNO_FUNCOES_EXECUCAO_KEYS, Union[RAM,
                                                                        REGISTRADORES, REGISTRADOR_INDEX, str, PIXEL_MAP]]
FUNCOES_EXECUCAO = Callable[[RAM, REGISTRADORES,
                             REGISTRADOR_INDEX, str, PIXEL_MAP], RETORNO_FUNCOES_EXECUCAO]
