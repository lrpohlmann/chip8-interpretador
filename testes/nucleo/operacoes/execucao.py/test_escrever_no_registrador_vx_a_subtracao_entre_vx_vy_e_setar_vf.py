from chip8.nucleo.operacoes.execucao.escrever_no_registrador_vx_a_subtracao_entre_vx_vy_e_setar_vf import escrever_no_registrador_vx_a_subtracao_entre_vx_vy_e_setar_vf
from testes.fixtures import setup_contexto_runtime


def test_escrever_no_registrador_vx_a_subtracao_entre_vx_vy_e_setar_vf(setup_contexto_runtime):
    input_e_output = [
        {
            "input": {
                "registradores": [("0", "1"), ("1", "1")]
            },
            "output": {
                "registradores": [("0", "0"), ("1", "1"), ("f", "0")]
            }
        },
        {
            "input": {
                "registradores": [("0", "3"), ("1", "f")]
            },
            "output": {
                "registradores": [("0", "0"), ("1", "f"), ("f", "1")]
            }
        }
    ]

    for _ in input_e_output:
        contexto = setup_contexto_runtime(
            registradores=_["input"]["registradores"])
        novo_contexto = escrever_no_registrador_vx_a_subtracao_entre_vx_vy_e_setar_vf(
            "0", "1", contexto)

        for endereco, valor in _["output"]["registradores"]:
            assert novo_contexto["registradores"][endereco] == valor
