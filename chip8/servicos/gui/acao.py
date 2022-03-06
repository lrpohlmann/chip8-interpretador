from chip8.nucleo.operacoes.codigo_contexto_runtime import ler_contexto_runtime
from chip8.nucleo.dados.tipos import CONTEXTO_RUNTIME, PIXEL_MAP
from chip8.servicos.gui import display
from chip8.servicos.gui.eventos import EventoProtocol, AtualizarDisplayProtocol


def atualizar_display(evento: AtualizarDisplayProtocol):
    pixel_map = evento.dados

    if display.display != None:
        for coord, pix in pixel_map.items():
            x, y = coord
            if pix == 1:
                display.desenhar_pixel_branco(x, y)
            elif pix == 0:
                display.desenhar_pixel_preto(x, y)
            else:
                raise Exception()

    display.atualizar_tela()
