from typing import Any
from chip8.nucleo.dados.type_alias import RAM, REGISTRADOR_INDEX, REGISTRADORES
from chip8.nucleo.operacoes.codigo_registradores import escrever_registrador_index
from chip8.nucleo.operacoes.type_alias import RETORNO_FUNCOES_EXECUCAO

from chip8.servicos import log_parametros_e_retorno_da_funcao


@log_parametros_e_retorno_da_funcao
def _escrever_no_registrador_index(dado: str, ram: RAM, registradores: REGISTRADORES, registrador_index: REGISTRADOR_INDEX, contador: str) -> RETORNO_FUNCOES_EXECUCAO:
    """Escreve um endereço no registrador index.

    Args:
        dado (str): endereço a ser escrito
        ram (RAM): memória RAM
        registradores (REGISTRADORES): Registradores
        registrador_index (REGISTRADOR_INDEX): Registrador index
        contador (str): Contador

    Returns:
        RETORNO_FUNCOES_EXECUCAO
    """
    registrador_index_escrito = escrever_registrador_index(
        registrador_index, dado)
    return ram, registradores, registrador_index_escrito, contador
