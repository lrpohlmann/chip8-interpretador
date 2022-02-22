from testes.fixtures import *
from chip8.nucleo.operacoes.execucao import _escrever_no_registrador_index


def test_escrever_no_registrador_index(ram: RAM, registradores: REGISTRADORES, registrador_index: REGISTRADOR_INDEX):
    resultado = _escrever_no_registrador_index(
        "300", ram, registradores, registrador_index, "200")
    assert resultado[2]["i"] == "300"
