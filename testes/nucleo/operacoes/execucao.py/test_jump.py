from chip8.nucleo.operacoes.execucao import _jump
from testes.fixtures import *


def test_jump(ram: RAM, registradores: REGISTRADORES, registrador_index: REGISTRADOR_INDEX):
    retorno = _jump("200", ram, registradores, registrador_index, "500")
    assert retorno[3] == "200"
