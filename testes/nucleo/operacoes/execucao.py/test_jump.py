from chip8.nucleo.operacoes.execucao import _jump
from testes.fixtures import *


def test_jump(ram: RAM, registradores: REGISTRADORES, registrador_index: REGISTRADOR_INDEX, pixel_map: PIXEL_MAP):
    retorno = _jump("200", ram, registradores,
                    registrador_index, "500", pixel_map)
    assert retorno["contador"] == "200"
