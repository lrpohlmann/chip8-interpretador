from chip8.servicos.hexadecimais.aritimetica import somar_hexadecimais, subtrair_hexadecimais


def test_somar():
    assert somar_hexadecimais("1", "1", "1") == "3"


def test_subtrair():
    assert subtrair_hexadecimais("4", "3") == "1"
