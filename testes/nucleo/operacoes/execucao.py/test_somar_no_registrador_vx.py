from testes.fixtures import *
from chip8.nucleo.operacoes.execucao import _somar_no_registrador_vx


def test_somar_no_registrador_vx(ram: RAM, registradores: REGISTRADORES, registrador_index: REGISTRADOR_INDEX):
    registradores["1"] = "1"
    resultado = _somar_no_registrador_vx(
        "1", "1", ram, registradores, registrador_index, "200")
    assert resultado[1]["1"] == "2"
