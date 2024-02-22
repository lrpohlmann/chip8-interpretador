from chip8.nucleo.instrucao import (
    escrever_no_registrador_vx_o_valor_vx_xor_vy_8XY3,
)
from testes.fixtures import setup_contexto_runtime


def test_vx_xor_vy(setup_contexto_runtime):
    setup_dados = [
        {"dados": [("0", "0"), ("1", "1")], "resultado": "1"},
        {"dados": [("0", "1"), ("1", "1")], "resultado": "0"},
    ]

    for dado in setup_dados:
        contexto = setup_contexto_runtime(registradores=dado["dados"])
        escrever_no_registrador_vx_o_valor_vx_xor_vy_8XY3("8013")(contexto)
        contexto.registradores["0"] == dado["resultado"]
