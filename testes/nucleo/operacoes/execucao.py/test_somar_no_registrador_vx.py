from immutables import Map
from testes.fixtures import *
from chip8.nucleo.operacoes.execucao import _somar_no_registrador_vx
from chip8.nucleo.operacoes import escrever_registrador
from chip8.nucleo.operacoes.codigo_contexto_runtime import escrever_contexto_runtime, ler_contexto_runtime


def test_somar_no_registrador_vx(contexto_runtime):
    registradores = ler_contexto_runtime(contexto_runtime, "registradores")
    registradores = escrever_registrador(registradores, "1", "1")
    novo_contexto = escrever_contexto_runtime(
        contexto_runtime, "registradores", registradores)
    resultado = _somar_no_registrador_vx(
        "1", "1", novo_contexto)
    assert resultado["registradores"]["1"] == "2"
    assert resultado["registrador_index"] == Map(i=None)
    assert resultado["contador"] == "200"
