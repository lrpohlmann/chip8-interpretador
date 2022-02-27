from typing import Dict

from chip8.nucleo.dados.tipos import *
from chip8.nucleo.operacoes.codigo_registradores import ler_registrador, escrever_registrador
from chip8.nucleo.operacoes.codigo_contexto_runtime import escrever_contexto_runtime, ler_contexto_runtime
from chip8.servicos.hexadecimais.aritimetica import somar_hexadecimais

from chip8.servicos import log_parametros_e_retorno_da_funcao


@log_parametros_e_retorno_da_funcao
def _somar_no_registrador_vx(endereco_registrador: str, dado_a_somar: str, contexto_runtime: CONTEXTO_RUNTIME) -> CONTEXTO_RUNTIME:
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

    registradores = ler_contexto_runtime(contexto_runtime, "registradores")

    soma = somar_hexadecimais(
        ler_registrador(registradores, endereco_registrador),
        dado_a_somar
    )

    registradores_escrito = escrever_registrador(
        registradores, endereco_registrador, soma
    )

    return escrever_contexto_runtime(
        contexto_runtime,
        "registradores",
        registradores_escrito
    )
