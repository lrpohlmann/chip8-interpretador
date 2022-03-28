from chip8.servicos.hexadecimais.aritimetica import somar_hexadecimais, subtrair_hexadecimais
from chip8.servicos.hexadecimais.bitwise import hexadecimal_bit_and, hexadecimal_bit_left_shift, hexadecimal_bit_right_shift, hexadecimal_bit_xor, hexadecimal_bit_or


def test_somar():
    input_e_resultados = [
        {
            "input": ["1", "1", "1"],
            "resultado": "3"
        },
        {
            "input": ["f", "f", "f", "f"],
            "resultado": "3c"
        },
        {
            "input": ["-3", "1"],
            "resultado": "-2"
        }
    ]

    for _ in input_e_resultados:
        assert somar_hexadecimais(*_["input"]) == _["resultado"]


def test_subtrair():
    input_e_resultados = [
        {
            "input": ["1", "1", "1"],
            "resultado": "-1"
        },
        {
            "input": ["f", "f", "f", "f"],
            "resultado": "-1e"
        },
        {
            "input": ["-3", "1"],
            "resultado": "-4"
        },
        {
            "input": ["5", "-1"],
            "resultado": "6"
        }
    ]

    for _ in input_e_resultados:
        assert subtrair_hexadecimais(*_["input"]) == _["resultado"]


def test_or():
    for input, output in {("0", "0"): "0", ("0", "1"): "1", ("1", "1"): "1"}.items():
        assert hexadecimal_bit_or(*input) == output


def test_and():
    for input, output in {("0", "0"): "0", ("0", "1"): "0", ("1", "1"): "1"}.items():
        assert hexadecimal_bit_and(*input) == output


def test_xor():
    for input, output in {("0", "0"): "0", ("0", "1"): "1", ("1", "1"): "0"}.items():
        assert hexadecimal_bit_xor(*input) == output


def test_left_shift():
    input_e_resultado = [
        {
            "input": "1",
            "resultado": "2",
        },
        {
            "input": "2",
            "resultado": "4",
        },
        {
            "input": "3",
            "resultado": "6"
        }
    ]

    for _ in input_e_resultado:
        assert hexadecimal_bit_left_shift(_["input"]) == _["resultado"]


def test_right_shift():
    input_e_resultado = [
        {
            "input": "1",
            "resultado": "0",
        },
        {
            "input": "2",
            "resultado": "1",
        },
        {
            "input": "3",
            "resultado": "1"
        }
    ]

    for _ in input_e_resultado:
        assert hexadecimal_bit_right_shift(_["input"]) == _["resultado"]
