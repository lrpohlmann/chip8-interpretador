from typing import Tuple
from typing import Union
import pygame

PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)


display: Union[pygame.Surface, None] = None


def setup_tela():
    global display
    pygame.init()
    display = pygame.display.set_mode(size=(64, 32))


def desenhar_pixel_branco(x, y):
    _desenhar_pixel(x, y, BRANCO)


def desenhar_pixel_preto(x, y):
    _desenhar_pixel(x, y, PRETO)


def _desenhar_pixel(x, y, cor: Tuple[int, int, int]):
    global display
    if isinstance(display, pygame.Surface):
        pygame.draw.rect(
            surface=display,
            color=cor,
            rect=pygame.rect.Rect(x, y, 1, 1)
        )
