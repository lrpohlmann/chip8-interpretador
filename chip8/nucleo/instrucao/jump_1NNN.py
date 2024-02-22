from functools import partial
from typing import Callable

from chip8.nucleo import ContextoRuntime


def _jump(pular_para: str, contexto_runtime: ContextoRuntime) -> ContextoRuntime:
    contexto_runtime.contador.atualizar(pular_para)
    return contexto_runtime


def jump_1NNN(instrucao: str) -> Callable[[ContextoRuntime], ContextoRuntime]:
    endereco_ram_para_pular = instrucao[1:]
    return partial(_jump, endereco_ram_para_pular)
