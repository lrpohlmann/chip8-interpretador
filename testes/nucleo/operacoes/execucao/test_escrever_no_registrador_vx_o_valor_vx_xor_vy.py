from chip8.nucleo.operacoes.execucao.escrever_no_registrador_vx_o_valor_vx_xor_vy import escrever_no_registrador_vx_o_valor_vx_xor_vy
from testes.fixtures import setup_contexto_runtime


def test_vx_xor_vy(setup_contexto_runtime):
    setup_dados = [
        {"dados": [("0", "0"), ("1", "1")], "resultado": "1"},
        {"dados": [("0", "1"), ("1", "1")], "resultado": "0"}
    ]

    for dado in setup_dados:
        contexto = setup_contexto_runtime(registradores=dado["dados"])
        novo_contexto = escrever_no_registrador_vx_o_valor_vx_xor_vy(
            "0", "1", contexto)
        novo_contexto["registradores"]["0"] == dado["resultado"]
