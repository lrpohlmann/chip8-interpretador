from typing import List, Sequence

from chip8.nucleo.dados.tipos import CALL_STACK, e_call_stack
from pyrsistent import pvector


def criar_call_stack() -> CALL_STACK:
    call_stack: Sequence[str] = pvector([])
    if e_call_stack(call_stack):
        return call_stack
    else:
        raise Exception()
