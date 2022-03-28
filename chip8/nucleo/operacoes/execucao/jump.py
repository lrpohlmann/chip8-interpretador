from typing import Dict
import immutables

from chip8.nucleo.dados.tipos import CONTADOR, CONTEXTO_RUNTIME
from chip8.nucleo.operacoes.codigo_contexto_runtime import escrever_contexto_runtime
from chip8.servicos import log_parametros_e_retorno_da_funcao


@log_parametros_e_retorno_da_funcao
def _jump(pular_para: CONTADOR, contexto_runtime: CONTEXTO_RUNTIME) -> CONTEXTO_RUNTIME:
    return escrever_contexto_runtime(contexto_runtime, "contador", pular_para)
