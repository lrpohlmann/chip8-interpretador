from immutables import Map
from chip8.nucleo.dados.tipos import PIXEL_MAP, PIXEL_MAP_COORDENADA_X, PIXEL_MAP_COORDENADA_Y, e_pixel_map
import itertools


def criar_pixel_map(largura: int = 64, altura: int = 32) -> PIXEL_MAP:
    coordenadas = [(PIXEL_MAP_COORDENADA_X(x), PIXEL_MAP_COORDENADA_Y(y)) for x, y in list(
        itertools.product(
            range(0, largura),
            range(0, altura)
        )
    )]

    with Map().mutate() as map:  # type: ignore
        for coord in coordenadas:
            map[coord] = 0

        pixel_map = map.finish()

    if e_pixel_map(pixel_map):
        return pixel_map
    else:
        raise Exception()
