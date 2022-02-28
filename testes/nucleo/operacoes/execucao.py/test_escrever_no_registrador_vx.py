from testes.fixtures import *
from chip8.nucleo.operacoes.execucao import _escrever_no_registrador_vx


def test_escrever_no_registrador_vx(contexto_runtime):
    resultado = _escrever_no_registrador_vx(
        "0", "f", contexto_runtime)
    assert resultado["registradores"]['0'] == "f"
    assert resultado["registrador_index"] == Map(i=None)
    assert resultado["contador"] == "200"
