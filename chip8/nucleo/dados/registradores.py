from immutables import Map

from chip8.nucleo.dados.tipos import REGISTRADOR_INDEX, REGISTRADORES, e_registrador, e_registrador_index
from chip8.servicos.inteiros.conversao import inteiros_para_hexadecimais


def criar_registradores(tamanho: int = 16) -> REGISTRADORES:
    registradores = Map(
        **dict(
            [(inteiros_para_hexadecimais(endereco), None)
             for endereco in range(0, tamanho)]
        )
    )

    if e_registrador(registradores):
        return registradores
    else:
        raise Exception()


def criar_registrador_index() -> REGISTRADOR_INDEX:
    i = Map(i=None)
    if e_registrador_index(i):
        return i
    else:
        raise Exception()
