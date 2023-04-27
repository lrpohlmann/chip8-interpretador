from chip8.nucleo.operacoes.execucao.subexecucao.aritmetica_com_registradores import aritimetica_entre_registrador_e_numero, aritimetica_entre_registradores
from testes.fixtures import setup_registradores


def test_aritmetica_com_registrador(setup_registradores):
    input_e_resultados_esperado = [
        {
            "input": {
                "numero_registrador": "2",
                "numero_para_operacao": "1",
                "operacao": "soma"
            },
            "resultados": {
                "operacao": "3",
            }
        },
        {
            "input": {
                "numero_registrador": "9",
                "numero_para_operacao": "6",
                "operacao": "soma"
            },
            "resultados": {
                "operacao": "f",
            }
        },
        {
            "input": {
                "numero_registrador": "2",
                "numero_para_operacao": "1",
                "operacao": "subtracao"
            },
            "resultados": {
                "operacao": "1",
            }
        },
        {
            "input": {
                "numero_registrador": "f",
                "numero_para_operacao": "e",
                "operacao": "subtracao"
            },
            "resultados": {
                "operacao": "1",
            }
        },
    ]

    for _ in input_e_resultados_esperado:
        registradores = setup_registradores(
            [("0", _["input"]["numero_registrador"])])
        novo_registrador = aritimetica_entre_registrador_e_numero(
            _["input"]["operacao"], registradores, "0", _["input"]["numero_para_operacao"])

        assert novo_registrador["0"] == _["resultados"]["operacao"]


def test_aritmetica_entre_registradores(setup_registradores):
    input_e_resultados_esperado = [
        {
            "input": {
                "registradores": [
                    ("0", "1"), ("1", "2")
                ],
                "operacao": "soma"
            },
            "resultados": {
                "registradores": [
                    ("0", "3"), ("1", "2")
                ]
            }
        },
        {
            "input": {
                "registradores": [
                    ("0", "9"), ("1", "6")
                ],
                "operacao": "soma"
            },
            "resultados": {
                "registradores": [
                    ("0", "f"), ("1", "6")
                ]
            }
        },
        {
            "input": {
                "registradores": [
                    ("0", "2"), ("1", "1")
                ],
                "operacao": "subtracao"
            },
            "resultados": {
                "registradores": [
                    ("0", "1"), ("1", "1")
                ]
            }
        },
        {
            "input": {
                "registradores": [
                    ("0", "9"), ("1", "5")
                ],
                "operacao": "subtracao"
            },
            "resultados": {
                "registradores": [
                    ("0", "4"), ("1", "5")
                ]
            }
        },
    ]

    for _ in input_e_resultados_esperado:
        registradores = setup_registradores(_["input"]["registradores"])
        novo_registrador = aritimetica_entre_registradores(
            _["input"]["operacao"], registradores, "0", "1")
        for k, v in _["resultados"]["registradores"]:
            assert novo_registrador[k] == v
