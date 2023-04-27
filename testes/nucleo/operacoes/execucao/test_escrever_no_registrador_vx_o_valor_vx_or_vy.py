from chip8.nucleo.operacoes.execucao.escrever_no_registrador_vx_o_valor_vx_or_vy import escrever_no_registrador_vx_o_valor_vx_or_vy
from testes.fixtures import setup_contexto_runtime


def test_escrever_no_registrador_vx_o_valor_vx_or_vy(setup_contexto_runtime):
    contexto_runtime = setup_contexto_runtime(
        registradores=[("0", "5"), ("1", "3")])
    novo_contexto = escrever_no_registrador_vx_o_valor_vx_or_vy(
        "0", "1", contexto_runtime)
    assert novo_contexto["registradores"]["0"] == "7"
