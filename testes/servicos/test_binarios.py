from chip8.servicos.binarios.conversao import binario_para_hexadecimal


def test_binario_para_hexadecimal():
    assert binario_para_hexadecimal("0b11111111") == "ff"
    assert binario_para_hexadecimal("11111111") == "ff"
