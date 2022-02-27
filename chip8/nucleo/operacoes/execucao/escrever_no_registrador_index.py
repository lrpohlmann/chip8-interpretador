from typing import Any
from chip8.nucleo.dados.tipos import PIXEL_MAP, RAM, REGISTRADOR_INDEX, REGISTRADORES, CONTEXTO_RUNTIME
from chip8.nucleo.operacoes.codigo_registradores import escrever_registrador_index
from chip8.nucleo.operacoes.codigo_contexto_runtime import ler_contexto_runtime, escrever_contexto_runtime


from chip8.servicos import log_parametros_e_retorno_da_funcao


@log_parametros_e_retorno_da_funcao
def _escrever_no_registrador_index(dado: str, contexto_runtime: CONTEXTO_RUNTIME) -> CONTEXTO_RUNTIME:
    """Escreve um endereço no registrador index.

    Args:
        dado (str): endereço a ser escrito
        ram (RAM): memória RAM
        registradores (REGISTRADORES): Registradores
        registrador_index (REGISTRADOR_INDEX): Registrador index
        contador (str): Contador

    Returns:
        CONTEXTO_RUNTIME
    """

    registrador_index = ler_contexto_runtime(
        contexto_runtime, "registrador_index")

    registrador_index_escrito = escrever_registrador_index(
        registrador_index, dado)
    return escrever_contexto_runtime(contexto_runtime, "registrador_index", registrador_index_escrito)
