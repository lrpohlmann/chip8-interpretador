from typing import Dict

from chip8.nucleo.operacoes.type_alias import RETORNO_FUNCOES_EXECUCAO
from chip8.nucleo.dados.type_alias import PIXEL_MAP, RAM, REGISTRADOR_INDEX, REGISTRADORES
from chip8.servicos import log_parametros_e_retorno_da_funcao


@log_parametros_e_retorno_da_funcao
def _jump(pular_para: str, ram: RAM, registradores: REGISTRADORES, registrador_index: REGISTRADOR_INDEX, contador: str, pixel_map: PIXEL_MAP) -> RETORNO_FUNCOES_EXECUCAO:
    """Altera o contador para o endereço informado.

    Args:
        pular_para (str): novo endereço do contador
        ram (RAM): memória RAM
        registradores (REGISTRADORES): Registradores
        registrador_index (REGISTRADOR_INDEX): Registrador index
        contador (str): Contador

    Returns:
        RETORNO_FUNCOES_EXECUCAO
    """
    contador = pular_para
    return {"ram": ram, "registradores": registradores, "registrador_index": registrador_index, "contador": contador, "pixel_map": pixel_map}
