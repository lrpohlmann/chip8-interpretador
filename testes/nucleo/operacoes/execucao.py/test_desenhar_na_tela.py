from chip8.nucleo.operacoes.execucao import _desenhar_na_tela
from testes.fixtures import *


def test_desenhar_na_tela(ram: RAM, registradores: REGISTRADORES, registrador_index: REGISTRADOR_INDEX):
    pixel_map = criar_pixel_map()
    registrador_index["i"] = "200"
    ram["200"] = "ff"
    ram["201"] = "ff"
    ram["202"] = "ff"
    registradores["0"] = "0"
    registradores["1"] = "0"
    ram, registradores, registrador_index, contador, pixel_map = _desenhar_na_tela("0", "1", "2", ram, registradores,
                                                                                   registrador_index, "200", pixel_map)

    for x in range(0, 8):
        for y in range(0, 3):
            assert pixel_map[(x, y)] == 1
            pixel_map.pop((x, y))

    for i in pixel_map.values():
        assert i == 0
