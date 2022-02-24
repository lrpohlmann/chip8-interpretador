from testes.fixtures import *
from chip8.nucleo.operacoes.execucao import _escrever_no_registrador_index


def test_escrever_no_registrador_index(ram: RAM, registradores: REGISTRADORES, registrador_index: REGISTRADOR_INDEX, pixel_map: PIXEL_MAP):
    resultado = _escrever_no_registrador_index(
        "300", ram, registradores, registrador_index, "200", pixel_map)
    assert resultado["registrador_index"]["i"] == "300"
    for k in resultado["registradores"].values():
        assert k == None
    assert resultado["contador"] == "200"
