from chip8.nucleo.operacoes.execucao.escrever_no_registrador_vy_o_valor_vx_left_bit_shifted import escrever_no_registrador_vy_o_valor_vx_left_bit_shifted
from testes.fixtures import setup_contexto_runtime


def test_escrever_no_registrador_vy_o_valor_vx_left_bit_shifted(setup_contexto_runtime):
    input_e_resultado = [
        {
            "input": {
                "registradores": [("0", "3"), ]
            },
            "output": {
                "registradores": [("0", "3"), ("1", "6"), ("f", "1")],
            }
        }
    ]

    for _ in input_e_resultado:
        contexto = setup_contexto_runtime(
            registradores=_["input"]["registradores"])
        novo_contexto = escrever_no_registrador_vy_o_valor_vx_left_bit_shifted(
            "0", "1", contexto)

        for endereco, valor in _["output"]["registradores"]:
            assert novo_contexto["registradores"][endereco] == valor
