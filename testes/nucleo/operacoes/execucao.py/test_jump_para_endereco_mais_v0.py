from chip8.nucleo.operacoes.execucao.jump_para_endereco_mais_v0 import jump_para_endereco_mais_v0
from testes.fixtures import setup_contexto_runtime


def test_jump_para_endereco_mais_v0(setup_contexto_runtime):
    input_e_output = [
        {
            "input": {
                "endereco": "100",
                "registradores": [("0", "200"), ],
                "contador": "0"
            },
            "output": {
                "registradores": [("0", "200"), ],
                "contador": "300"
            }
        },
        {
            "input": {
                "endereco": "40f",
                "registradores": [("0", "f"), ],
                "contador": "0"
            },
            "output": {
                "registradores": [("0", "f"), ],
                "contador": "41e"
            }
        }
    ]

    for _ in input_e_output:
        contexto = setup_contexto_runtime(
            registradores=_["input"]["registradores"], contador=_["input"]["contador"])
        novo_contexto = jump_para_endereco_mais_v0(
            _["input"]["endereco"], "0", contexto)

        for endereco, valor in _["output"]["registradores"]:
            assert novo_contexto["registradores"][endereco] == valor

        assert novo_contexto["contador"] == _["output"]["contador"]
