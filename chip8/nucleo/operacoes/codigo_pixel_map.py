from typing import Literal
from operator import xor

from pyrsistent import pmap

from chip8.nucleo.dados.tipos import (
    PIXEL_MAP,
    PIXEL_MAP_COORDENADA_X,
    PIXEL_MAP_COORDENADA_Y,
    SPRITE,
    e_pixel_map,
)
from chip8.servicos.hexadecimais.conversao import hexadecimal_para_inteiro


def _ler_pixel_map(pixel_map: PIXEL_MAP, coord_x: int, coord_y: int) -> Literal[0, 1]:
    try:
        return pixel_map[
            (PIXEL_MAP_COORDENADA_X(coord_x), PIXEL_MAP_COORDENADA_Y(coord_y))
        ]
    except KeyError:
        raise Exception(
            f"PIXEL MAP: coordenada {(coord_x, coord_y)} de píxel desconhecida."
        )


def _escrever_pixel_map(
    pixel_map: PIXEL_MAP, coord_x: int, coord_y: int, dado: Literal[0, 1]
) -> PIXEL_MAP:
    try:
        pixel_map_escrito = pixel_map.set(
            (PIXEL_MAP_COORDENADA_X(coord_x), PIXEL_MAP_COORDENADA_Y(coord_y)), dado
        )
        if e_pixel_map(pixel_map_escrito):
            return pixel_map_escrito
        else:
            raise Exception()
    except KeyError:
        raise Exception(
            f"PIXEL MAP: coordenada {(coord_x, coord_y)} de píxel desconhecida."
        )


def inserir_sprite_no_pixel_map(
    pixel_map: PIXEL_MAP, coord_x_inicial: str, coord_y_inicial: str, sprite: SPRITE
) -> PIXEL_MAP:
    for numero_linha_do_sprite, linha_do_sprite in enumerate(sprite):
        coord_y_onde_inserir = (
            hexadecimal_para_inteiro(coord_y_inicial) + numero_linha_do_sprite
        )
        for numero_bit_do_sprite, bit_do_sprite in enumerate(linha_do_sprite):
            coord_x_onde_inserir = (
                hexadecimal_para_inteiro(coord_x_inicial) + numero_bit_do_sprite
            )
            pixel_map = _inserir_bit_como_pixel(
                pixel_map,
                coord_x_onde_inserir,
                coord_y_onde_inserir,
                int(bit_do_sprite),
            )  # type: ignore

    return pixel_map


def zerar_pixel_map(pixel_map: PIXEL_MAP) -> PIXEL_MAP:
    mutar = {}
    for coodernadas in pixel_map.keys():
        mutar[coodernadas] = 0

    pixel_map_zerado = pmap(mutar)

    if e_pixel_map(pixel_map_zerado):
        return pixel_map_zerado
    else:
        raise Exception()


def _inserir_bit_como_pixel(
    pixel_map: PIXEL_MAP, x: int, y: int, bit: Literal[0, 1]
) -> PIXEL_MAP:
    pixel: Literal[0, 1] = _xor_pixel_bit(_ler_pixel_map(pixel_map, x, y), bit)

    return _escrever_pixel_map(pixel_map, x, y, pixel)


def _xor_pixel_bit(atual: Literal[0, 1], bit: Literal[0, 1]) -> Literal[0, 1]:
    pixel = xor(atual, bit)
    if pixel not in (0, 1):
        raise Exception(
            f"PIXEL MAP: bit inválido: xor({atual}, {bit}) == {pixel} != 0 ou 1"
        )

    return pixel
