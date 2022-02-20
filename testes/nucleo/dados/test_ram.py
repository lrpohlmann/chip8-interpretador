from operator import eq
from chip8.nucleo.dados.ram import criar_memoria_ram


def test_criacao_ram():
    ram = criar_memoria_ram(4096)

    assert eq(max(ram.keys()), "fff")
