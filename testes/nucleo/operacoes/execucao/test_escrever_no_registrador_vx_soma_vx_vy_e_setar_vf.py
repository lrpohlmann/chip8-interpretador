from chip8.nucleo.operacoes.execucao.escrever_no_registrador_vx_a_soma_vx_e_vy_e_setar_vf import escrever_no_registrador_vx_a_soma_vx_e_vy_e_setar_vf
from testes.fixtures import setup_contexto_runtime


def test_somar_vx_vy_e_setar_vf(setup_contexto_runtime):
    input_output = [
        {
            "input": {
                "registradores": [
                    ("0", "1"), ("1", "1")
                ]
            },
            "output": {"registradores": [
                ("0", "2"), ("1", "1"), ("f", "0")
            ]}
        },
        {
            "input": {
                "registradores": [
                    ("0", "ff"), ("1", "1")
                ]
            },
            "output": {
                "registradores": [
                    ("0", "ff"), ("1", "1"), ("f", "1")
                ]
            }
        }
    ]

    for in_out in input_output:
        contexto = setup_contexto_runtime(
            registradores=in_out["input"]["registradores"])
        novo_contexto = escrever_no_registrador_vx_a_soma_vx_e_vy_e_setar_vf(
            "0", "1", contexto)

        for k, v in in_out["output"]["registradores"]:
            assert novo_contexto["registradores"][k] == v
