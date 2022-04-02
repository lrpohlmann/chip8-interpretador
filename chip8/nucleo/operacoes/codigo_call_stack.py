from sre_constants import CALL
from typing import List, NoReturn, Tuple
from pyrsistent.typing import PVector
from functools import singledispatch

from chip8.nucleo.dados.tipos import CALL_STACK, e_call_stack


def obter_valor_topo_da_stack(call_stack: CALL_STACK) -> Tuple[CALL_STACK, str]:
    return _pop_stack(call_stack)


def _pop_stack(call_stack: CALL_STACK) -> Tuple[CALL_STACK, str]:
    endereco = call_stack[-1]
    call_stack_novo = _remover_elemento_stack(call_stack)
    return call_stack_novo, endereco


def _remover_elemento_stack(call_stack: CALL_STACK) -> CALL_STACK:
    call_stack_novo = call_stack.delete(len(call_stack) - 1)  # type: ignore
    if e_call_stack(call_stack_novo):
        return call_stack_novo
    else:
        raise Exception()


def adicionar_valor_topo_da_stack(call_stack: CALL_STACK, valor: str) -> CALL_STACK:
    call_stack_novo = _append_stack(call_stack, valor)
    return call_stack_novo


def _append_stack(call_stack: CALL_STACK, valor: str) -> CALL_STACK:
    call_stack_novo = call_stack.append(valor)
    if e_call_stack(call_stack_novo):
        return call_stack_novo
    else:
        raise Exception()
