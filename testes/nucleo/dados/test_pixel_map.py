from testes.fixtures import *
from chip8.nucleo.dados import criar_pixel_map
from chip8.nucleo.dados import PIXEL_MAP_COORDENADA_X, PIXEL_MAP_COORDENADA_Y


def test_criar_pixel_map():
    pixel_map = criar_pixel_map()
    assert len(set([coord[0] for coord in pixel_map.keys()])) == 64
    assert len(set([coord[1] for coord in pixel_map.keys()])) == 32
