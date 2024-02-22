from functools import partial
from typing import Callable

from chip8.nucleo import ContextoRuntime, ENDERECO_REGISTRADORES
from chip8.nucleo.instrucao.subinstrucao.aritmetica_com_registradores import (
    aritimetica_entre_registrador_e_numero,
)


def somar_no_registrador_vx_7XNN(
    instrucao: str,
) -> Callable[[ContextoRuntime], ContextoRuntime]:
    endereco_registrador = instrucao[1]
    dado = instrucao[2:]
    return partial(_somar_no_registrador_vx, endereco_registrador, dado)


def _somar_no_registrador_vx(
    endereco_registrador: ENDERECO_REGISTRADORES,
    dado_a_somar: str,
    contexto_runtime: ContextoRuntime,
) -> ContextoRuntime:
    contexto_runtime.registradores = aritimetica_entre_registrador_e_numero(
        "soma", contexto_runtime.registradores, endereco_registrador, dado_a_somar
    )
    return contexto_runtime
