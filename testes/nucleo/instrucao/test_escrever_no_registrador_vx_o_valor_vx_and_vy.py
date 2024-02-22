from chip8.nucleo.instrucao import (
    escrever_no_registrador_vx_o_valor_vx_and_vy_8XY2,
)
from testes.fixtures import setup_contexto_runtime


def test_escrever_no_registrador_vx_o_valor_vx_and_vy(setup_contexto_runtime):
    contexto = setup_contexto_runtime(registradores=[("0", "1"), ("1", "0")])
    escrever_no_registrador_vx_o_valor_vx_and_vy_8XY2("8012")(contexto)
    assert contexto.registradores["0"] == "0"
