from operator import eq

from chip8.nucleo.dados.registradores import criar_registradores
from chip8.servicos.inteiros.conversao import inteiros_para_hexadecimais


def test_criar_registradores():
    registradores = criar_registradores(16)

    assert all([eq(x, None) for x in registradores.values()])
    assert eq(max(registradores.keys()), inteiros_para_hexadecimais(15))
