from typing import Container, Sequence
from chip8.nucleo.dados.call_stack import criar_call_stack


def test_criar_call_stack():
    st = criar_call_stack()
    assert isinstance(st, Sequence)
