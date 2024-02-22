from testes.fixtures import *
from chip8.nucleo.instrucao import somar_no_registrador_vx_7XNN


def test_somar_no_registrador_vx(contexto_runtime):
    contexto_runtime.registradores["1"] = "1"
    somar_no_registrador_vx_7XNN("711")(contexto_runtime)
    assert contexto_runtime.registradores["1"] == "2"
