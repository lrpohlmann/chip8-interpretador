from immutables import Map
from chip8.servicos.inteiros.conversao import inteiros_para_hexadecimais
from chip8.nucleo.dados.tipos import RAM, e_ram


def criar_memoria_ram(tamanho: int = 4096) -> RAM:
    ram = Map(
        **dict(
            [(inteiros_para_hexadecimais(n), None) for n in range(0, tamanho)]
        )
    )
    if e_ram(ram):
        return ram
    else:
        raise Exception()
