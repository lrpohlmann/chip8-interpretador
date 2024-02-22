from typing import Callable
from functools import partial

from chip8.nucleo import ContextoRuntime, ENDERECO_REGISTRADORES


def escrever_no_registrador_vx_6XNN(
    instrucao: str,
) -> Callable[[ContextoRuntime], ContextoRuntime]:
    endereco_registrador = instrucao[1]
    dado = instrucao[2:]
    return partial(_escrever_no_registrador_vx, endereco_registrador, dado)


def _escrever_no_registrador_vx(
    endereco_registrador: ENDERECO_REGISTRADORES,
    dado: str,
    contexto_runtime: ContextoRuntime,
) -> ContextoRuntime:
    contexto_runtime.registradores[endereco_registrador] = dado
    return contexto_runtime
