from testes.fixtures import *
from chip8.nucleo.operacoes.execucao import _escrever_no_registrador_index


def test_escrever_no_registrador_index(contexto_runtime):
    resultado = _escrever_no_registrador_index(
        "300", contexto_runtime)
    assert resultado["registrador_index"]["i"] == "300"
    for k in resultado["registradores"].values():
        assert k == None
    assert resultado["contador"] == "200"
