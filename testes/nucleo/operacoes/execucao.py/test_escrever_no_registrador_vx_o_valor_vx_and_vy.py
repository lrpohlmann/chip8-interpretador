from chip8.nucleo.operacoes.execucao.escrever_no_registrador_vx_o_valor_vx_and_vy import escrever_no_registrador_vx_o_valor_vx_and_vy
from testes.fixtures import setup_contexto_runtime


def test_escrever_no_registrador_vx_o_valor_vx_and_vy(setup_contexto_runtime):
    contexto = setup_contexto_runtime(registradores=[("0", "1"), ("1", "0")])
    novo_contexto = escrever_no_registrador_vx_o_valor_vx_and_vy(
        "0", "1", contexto)
    assert novo_contexto["registradores"]["0"] == "0"
