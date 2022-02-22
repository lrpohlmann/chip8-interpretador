from chip8.nucleo.dados.type_alias import PIXEL_MAP, PIXEL_MAP_COORDENADA_X, PIXEL_MAP_COORDENADA_Y
import itertools


def criar_pixel_map(largura: int = 64, altura: int = 32) -> PIXEL_MAP:
    coordenadas = [(PIXEL_MAP_COORDENADA_X(x), PIXEL_MAP_COORDENADA_Y(y)) for x, y in list(
        itertools.product(
            range(0, largura),
            range(0, altura)
        )
    )]

    return dict([(coord, 0) for coord in coordenadas])
