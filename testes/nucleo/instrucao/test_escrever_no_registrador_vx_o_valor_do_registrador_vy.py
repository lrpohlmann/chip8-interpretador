from chip8.nucleo.instrucao import (
    escrever_no_registrador_vx_o_valor_do_registrador_vy_8XY0,
)
from testes.fixtures import setup_contexto_runtime


def test_escrever_no_registrador_vx_o_valor_do_registrador_vy(setup_contexto_runtime):
    contexto = setup_contexto_runtime(registradores=[("0", None), ("1", "1")])
    escrever_no_registrador_vx_o_valor_do_registrador_vy_8XY0("8010")(contexto)
    assert contexto.registradores["0"] == "1"
