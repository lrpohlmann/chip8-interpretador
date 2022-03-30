from chip8.nucleo.operacoes.execucao.escrever_no_vy_o_valor_vx_right_bit_shifted import escrever_no_vy_o_valor_vx_right_bit_shifted
from testes.fixtures import setup_contexto_runtime


def test_escrever_no_vy_o_valor_vx_right_bit_shifted(setup_contexto_runtime):
    input_e_resultado = [
        {
            "input": {
                "registradores": [("0", "6"), ]
            },
            "resultado": {
                "registradores": [("0", "6"), ("1", "3"), ("f", "0")]
            }
        },
        {
            "input": {
                "registradores": [("0", "1"), ]
            },
            "resultado": {
                "registradores": [("0", "1"), ("1", "0"), ("f", "1")]
            }
        }
    ]

    for _ in input_e_resultado:
        contexto = setup_contexto_runtime(
            registradores=_["input"]["registradores"])
        novo_contexto = escrever_no_vy_o_valor_vx_right_bit_shifted(
            "0", "1", contexto)

        for endereco, valor in _["resultado"]["registradores"]:
            assert novo_contexto["registradores"][endereco] == valor
