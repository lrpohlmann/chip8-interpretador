from testes.fixtures import *
from chip8.nucleo.instrucao import escrever_no_registrador_vx_6XNN


def test_escrever_no_registrador_vx(contexto_runtime):
    escrever_no_registrador_vx_6XNN("60f")(contexto_runtime)
    assert contexto_runtime.registradores["0"] == "f"
    assert contexto_runtime.registradores.i == None
    assert contexto_runtime.contador == "200"
