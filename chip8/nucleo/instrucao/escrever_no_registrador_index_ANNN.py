from functools import partial
from typing import Callable

from chip8.nucleo import ContextoRuntime


def escrever_no_registrador_index_ANNN(
    instrucao: str,
) -> Callable[[ContextoRuntime], ContextoRuntime]:
    endereco = instrucao[1:]
    return partial(_escrever_no_registrador_index, endereco)


def _escrever_no_registrador_index(
    dado: str, contexto_runtime: ContextoRuntime
) -> ContextoRuntime:
    contexto_runtime.registradores.i = dado
    return contexto_runtime
