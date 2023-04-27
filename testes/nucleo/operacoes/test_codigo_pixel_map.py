from chip8.servicos import map
from chip8.nucleo.dados.tipos import SPRITE
from chip8.nucleo.operacoes import inserir_sprite_no_pixel_map
from chip8.nucleo.dados import criar_pixel_map
from chip8.nucleo.operacoes.codigo_pixel_map import zerar_pixel_map


def test_inserir_sprite():
    pixel_map = criar_pixel_map()
    sprite: SPRITE = ["11111111", "11111111"]
    pixel_map = inserir_sprite_no_pixel_map(pixel_map, "0", "0", sprite)
    for x in range(0, 8):
        for y in range(0, len(sprite)):
            assert pixel_map[(x, y)] == 1


def test_zerar_pixel_map():
    pixel_map = criar_pixel_map()

    def _1(pixel_map):
        dicio_1 = {k: 1 for k in pixel_map.keys()}
        return map.atualizar(pixel_map, dicio_1)

    pixel_map_1 = _1(pixel_map)

    pixel_map_zerado = zerar_pixel_map(pixel_map_1)

    assert set(pixel_map_zerado.values()) == {
        0,
    }
