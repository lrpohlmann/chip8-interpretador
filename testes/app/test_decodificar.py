from operator import eq
from typing import Callable
from chip8.app.decodificar import decodificar
from chip8.nucleo.operacoes.decodificadores._DXYN import decoder_DXYN


def test_decodificar():
    assert isinstance(decodificar('d01f'), Callable)
