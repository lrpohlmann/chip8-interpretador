from chip8.servicos.inteiros.conversao import inteiros_para_hexadecimais


def test_inteiros_para_hexa():
    for n in range(0, 10):
        assert inteiros_para_hexadecimais(n) == str(n)

    assert inteiros_para_hexadecimais(10) == "a"
    assert inteiros_para_hexadecimais(11) == "b"
    assert inteiros_para_hexadecimais(12) == "c"
    assert inteiros_para_hexadecimais(13) == "d"
    assert inteiros_para_hexadecimais(14) == "e"
    assert inteiros_para_hexadecimais(15) == "f"
