from testes.fixtures import *
from chip8.nucleo.operacoes.execucao import _somar_no_registrador_vx
from chip8.nucleo.operacoes import escrever_registrador


def test_somar_no_registrador_vx(contexto_runtime):
    novo_contexto = contexto_runtime.set("registradores", escrever_registrador(
        contexto_runtime["registradores"], "1", "1"))
    resultado = _somar_no_registrador_vx(
        "1", "1", novo_contexto)
    assert resultado["registradores"]["1"] == "2"
    assert resultado["registrador_index"] == {"i": None}
    assert resultado["contador"] == "200"
