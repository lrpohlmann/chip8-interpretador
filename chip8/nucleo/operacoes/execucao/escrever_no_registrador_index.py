from typing import Any
from chip8.nucleo.dados.type_alias import RAM, REGISTRADOR_INDEX, REGISTRADORES
from chip8.nucleo.operacoes.codigo_registradores import escrever_registrador_index

from chip8.servicos import log_parametros_e_retorno_da_funcao


@log_parametros_e_retorno_da_funcao
def _escrever_no_registrador_index(dado: Any, ram: RAM, registradores: REGISTRADORES, registrador_index: REGISTRADOR_INDEX, contador: str):
    registrador_index_escrito = escrever_registrador_index(
        registrador_index, dado)
    return ram, registradores, registrador_index_escrito, contador
