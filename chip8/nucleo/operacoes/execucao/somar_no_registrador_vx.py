
from chip8.nucleo.dados.tipos import *
from chip8.nucleo.operacoes.codigo_contexto_runtime import atualizar_contexto_runtime
from chip8.nucleo.operacoes.execucao.subexecucao.aritmetica_com_registradores import aritimetica_entre_registrador_e_numero

from chip8.servicos import log_parametros_e_retorno_da_funcao


@log_parametros_e_retorno_da_funcao
def _somar_no_registrador_vx(endereco_registrador: str, dado_a_somar: str, contexto_runtime: CONTEXTO_RUNTIME) -> CONTEXTO_RUNTIME:
    contexto_atualizado = atualizar_contexto_runtime(
        contexto_runtime,
        "registradores",
        lambda reg: aritimetica_entre_registrador_e_numero("soma", reg, endereco_registrador, dado_a_somar))

    return contexto_atualizado
