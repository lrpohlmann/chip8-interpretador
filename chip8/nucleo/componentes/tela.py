import itertools
from operator import xor
from typing import Literal
import os


class Tela:
    def __init__(self, largura: int = 64, altura: int = 32) -> None:
        self.LARGURA = largura
        self.ALTURA = altura
        self._pixels: dict[tuple[int, int], Literal[0, 1]] = {
            (x, y): 0
            for x, y in list(
                itertools.product(range(0, self.LARGURA), range(0, self.ALTURA))
            )
        }
        self.pixel_mudou_1_para_0 = False

    def desenhar_sprite(self, sprite: list[str], coord_x: str, coord_y: str):
        x = int(coord_x, 16)
        y = int(coord_y, 16)

        for numero_linha_do_sprite, linha_do_sprite in enumerate(sprite):
            for numero_bit_do_sprite, bit_do_sprite in enumerate(linha_do_sprite):
                coord_y_onde_inserir = y + numero_linha_do_sprite
                coord_x_onde_inserir = x + numero_bit_do_sprite

                bit = int(bit_do_sprite)
                assert bit in (0, 1)

                pixel_atual = self._pixels[(coord_x_onde_inserir, coord_y_onde_inserir)]
                pixel_xor = xor(
                    pixel_atual,
                    bit,
                )
                self._pixels[(coord_x_onde_inserir, coord_y_onde_inserir)] = pixel_xor

                if (pixel_atual == 1) and (pixel_xor == 0):
                    self.pixel_mudou_1_para_0 = True

        os.system("clear")
        print(self)

    def limpar_tela(self):
        for x in range(0, self.LARGURA):
            for y in range(0, self.ALTURA):
                self._pixels[(x, y)] = 0

    def __getitem__(self, __key: tuple[int, int]) -> Literal[0, 1]:
        if __key not in self._pixels.keys():
            raise Exception(f"Tela: Pixel desconhecido: {__key}")

        return self._pixels[__key]

    def __setitem__(self, __key: tuple[int, int], __value: Literal[0, 1]):
        if __key not in self._pixels.keys():
            raise Exception(f"Tela: Pixel desconhecido: {__key}")

        if __value not in (0, 1):
            raise Exception(f"Tela: Valor pixel inválido: {__value}")

        self._pixels[__key] = __value

    def __str__(self) -> str:
        s = ""
        for h in range(0, self.ALTURA):
            for x in range(0, self.LARGURA):
                pixel = " "
                if self._pixels[(x, h)]:
                    pixel = "█"

                s += pixel

            s += "\n"

        return s

    def __repr__(self) -> str:
        return (
            f"Altura: {self.ALTURA}, Largura: {self.LARGURA}, {self._pixels.__repr__()}"
        )
