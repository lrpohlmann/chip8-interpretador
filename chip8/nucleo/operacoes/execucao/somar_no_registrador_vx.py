from typing import Dict

from chip8.nucleo.dados.type_alias import *
from chip8.nucleo.operacoes.codigo_registradores import ler_registrador, escrever_registrador
from chip8.nucleo.operacoes.type_alias import CONTEXTO_RUNTIME
from chip8.servicos.hexadecimais.aritimetica import somar_hexadecimais

from chip8.servicos import log_parametros_e_retorno_da_funcao


@log_parametros_e_retorno_da_funcao
def _somar_no_registrador_vx(endereco_registrador: str, dado_a_somar: str, ram: RAM, registradores: REGISTRADORES, registrador_index: REGISTRADOR_INDEX, contador: str, pixel_map: PIXEL_MAP) -> CONTEXTO_RUNTIME:
    """Soma o valor dado com o valor escrite no registrador VX.

    Args:
        endereco_registrador (str): endereço do registrador VX
        dado_a_somar (str): valor a somar
        ram (RAM): memória RAM
        registradores (REGISTRADORES): Registradores
        registrador_index (REGISTRADOR_INDEX): Registrador index
        contador (str): Contador

    Returns:
        CONTEXTO_RUNTIME
    """
    registradores_escrito = escrever_registrador(
        registradores, endereco_registrador, somar_hexadecimais(
            ler_registrador(registradores, endereco_registrador),
            dado_a_somar
        )
    )

    return {"ram": ram, "registradores": registradores_escrito, "registrador_index": registrador_index, "contador": contador, "pixel_map": pixel_map}
