from typing import Dict

from chip8.nucleo.dados.type_alias import PIXEL_MAP, RAM, REGISTRADOR_INDEX, REGISTRADORES
from chip8.nucleo.operacoes.type_alias import RETORNO_FUNCOES_EXECUCAO
from chip8.nucleo.operacoes.codigo_registradores import escrever_registrador

from chip8.servicos import log_parametros_e_retorno_da_funcao


@log_parametros_e_retorno_da_funcao
def _escrever_no_registrador_vx(endereco_registrador: str, dado: str, ram: RAM, registradores: REGISTRADORES, registrador_index: REGISTRADOR_INDEX, contador: str, pixel_map: PIXEL_MAP) -> RETORNO_FUNCOES_EXECUCAO:
    """Escreve um dado no registrador VX.

    Args:
        endereco_registrador (str): endereço registrador VX.
        dado (str): dado a ser escrito
        ram (RAM): memória RAM
        registradores (REGISTRADORES): Registradores
        registrador_index (REGISTRADOR_INDEX): Registrador index
        contador (str): Contador

    Returns:
        RETORNO_FUNCOES_EXECUCAO
    """
    registradores_escrito = escrever_registrador(
        registradores, endereco_registrador, dado)
    return {"ram": ram, "registradores": registradores_escrito, "registrador_index": registrador_index, "contador": contador, "pixel_map": pixel_map}
