from typing import Any
from chip8.nucleo.dados.tipos import PIXEL_MAP, RAM, REGISTRADOR_INDEX, REGISTRADORES, CONTEXTO_RUNTIME
from chip8.nucleo.operacoes.codigo_registradores import escrever_registrador_index
from chip8.nucleo.operacoes.codigo_contexto_runtime import ler_contexto_runtime, escrever_contexto_runtime, atualizar_contexto_runtime


from chip8.servicos import log_parametros_e_retorno_da_funcao


@log_parametros_e_retorno_da_funcao
def _escrever_no_registrador_index(dado: str, contexto_runtime: CONTEXTO_RUNTIME) -> CONTEXTO_RUNTIME:
    return atualizar_contexto_runtime(contexto_runtime, "registrador_index", lambda i: escrever_registrador_index(i, dado))
