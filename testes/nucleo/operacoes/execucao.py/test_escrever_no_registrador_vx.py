from testes.fixtures import *
from chip8.nucleo.operacoes.execucao import _escrever_no_registrador_vx


def test_escrever_no_registrador_vx(ram: RAM, registradores: REGISTRADORES, registrador_index: REGISTRADOR_INDEX):
    resultado = _escrever_no_registrador_vx(
        "0", "f", ram, registradores, registrador_index, "200")
    assert resultado[1]['0'] == "f"
