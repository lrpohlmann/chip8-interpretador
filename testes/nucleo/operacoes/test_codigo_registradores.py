from chip8.nucleo.operacoes.codigo_registradores import escrever_registrador, ler_registrador, ler_registrador_index, escrever_registrador_index
from chip8.servicos.inteiros.conversao import inteiros_para_hexadecimais
from testes.fixtures import *


def test_escrever_registrador(registradores: REGISTRADORES):
    registrador_escrito = escrever_registrador(registradores, 0, "ff")
    assert registrador_escrito[inteiros_para_hexadecimais(0)] == "ff"


def test_ler_registrador(registradores: REGISTRADORES):
    registradores = registradores.set(inteiros_para_hexadecimais(0), "ff")
    assert ler_registrador(registradores, 0) == "ff"
    assert ler_registrador(registradores, "0") == "ff"


def test_ler_registrador_index(registrador_index: REGISTRADOR_INDEX):
    registrador_index = registrador_index.set("i", "111")
    assert ler_registrador_index(registrador_index) == '111'


def test_escrever_registrador_index(registrador_index: REGISTRADOR_INDEX):
    registrador_index = escrever_registrador_index(registrador_index, "111")
    assert registrador_index["i"] == "111"
