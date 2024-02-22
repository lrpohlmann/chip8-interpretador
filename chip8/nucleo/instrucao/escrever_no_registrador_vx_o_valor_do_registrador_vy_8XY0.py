from functools import partial
from typing import Callable

from chip8.nucleo import ContextoRuntime, ENDERECO_REGISTRADORES


def escrever_no_registrador_vx_o_valor_do_registrador_vy_8XY0(
    instrucao: str,
) -> Callable[[ContextoRuntime], ContextoRuntime]:
    vx = instrucao[1]
    vy = instrucao[2]
    return partial(_escrever_no_registrador_vx_o_valor_do_registrador_vy, vx, vy)


def _escrever_no_registrador_vx_o_valor_do_registrador_vy(
    endereco_vx: ENDERECO_REGISTRADORES,
    endereco_vy: ENDERECO_REGISTRADORES,
    contexto_runtime: ContextoRuntime,
) -> ContextoRuntime:
    contexto_runtime.registradores[endereco_vx] = contexto_runtime.registradores[
        endereco_vy
    ]
    return contexto_runtime
