from typing import Any, Dict, Literal, Protocol
import pygame

from chip8.nucleo.dados.tipos import CONTEXTO_RUNTIME, PIXEL_MAP
from chip8.servicos.gui import display


class EventoProtocol(Protocol):
    type: int
    dados: Any


class AtualizarDisplayProtocol(EventoProtocol):
    type: Literal[1000]
    dados: PIXEL_MAP


ID_TIPO_EVENTO_ATUALIZAR_DISPLAY = pygame.event.custom_type()


def emitir_evento_atualizar_display(pixel_map: PIXEL_MAP):
    if display.display:
        evento = _criar_evento(ID_TIPO_EVENTO_ATUALIZAR_DISPLAY, pixel_map)
        _emitir_evento(evento)


def _emitir_evento(evento):
    pygame.event.post(evento)


def _criar_evento(id_tipo_evento: int, dados: Any) -> EventoProtocol:
    evento = pygame.event.Event(id_tipo_evento, dados=dados)
    return evento
