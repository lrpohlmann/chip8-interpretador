from chip8.nucleo.operacoes.codigo_registradores import escrever_registrador, ler_registrador
from chip8.servicos.inteiros.conversao import inteiros_para_hexadecimais
from testes.fixtures import *


def test_escrever_registrador(registradores: REGISTRADORES):
    registrador_escrito = escrever_registrador(registradores, 0, "ff")
    assert registrador_escrito[inteiros_para_hexadecimais(0)] == "ff"


def test_ler_registrador(registradores: REGISTRADORES):
    registradores[inteiros_para_hexadecimais(0)] = "ff"
    assert ler_registrador(registradores, 0) == "ff"
    assert ler_registrador(registradores, "0") == "ff"
