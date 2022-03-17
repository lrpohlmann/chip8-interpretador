from chip8.servicos.hexadecimais.aritimetica import somar_hexadecimais, subtrair_hexadecimais
from chip8.servicos.hexadecimais.bitwise import hexadecimal_bit_and, hexadecimal_bit_xor, hexadecimal_bit_or


def test_somar():
    assert somar_hexadecimais("1", "1", "1") == "3"


def test_subtrair():
    assert subtrair_hexadecimais("4", "3") == "1"


def test_or():
    for input, output in {("0", "0"): "0", ("0", "1"): "1", ("1", "1"): "1"}.items():
        assert hexadecimal_bit_or(*input) == output


def test_and():
    for input, output in {("0", "0"): "0", ("0", "1"): "0", ("1", "1"): "1"}.items():
        assert hexadecimal_bit_and(*input) == output


def test_xor():
    for input, output in {("0", "0"): "0", ("0", "1"): "1", ("1", "1"): "0"}.items():
        assert hexadecimal_bit_xor(*input) == output
