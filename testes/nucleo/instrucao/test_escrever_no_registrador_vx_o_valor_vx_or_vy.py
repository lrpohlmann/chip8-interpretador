from chip8.nucleo.instrucao import (
    escrever_no_registrador_vx_o_valor_vx_or_vy_8XY1,
)
from testes.fixtures import setup_contexto_runtime


def test_escrever_no_registrador_vx_o_valor_vx_or_vy(setup_contexto_runtime):
    contexto_runtime = setup_contexto_runtime(registradores=[("0", "5"), ("1", "3")])
    escrever_no_registrador_vx_o_valor_vx_or_vy_8XY1("8011")(contexto_runtime)
    assert contexto_runtime.registradores["0"] == "7"
