from functools import reduce
import pygame
from chip8.app.obter_decodificar_executar_loop import obter_decodificar_executar
from chip8.nucleo.dados.tipos import CONTEXTO_RUNTIME

from chip8.nucleo.operacoes.obter.obter import obter
from chip8.nucleo.operacoes.decodificadores.decodificar import decodificar
from chip8.nucleo.operacoes.execucao.execucao import executar
from chip8.servicos.gui.acao import atualizar_display
from chip8.servicos.gui.eventos import ID_TIPO_EVENTO_ATUALIZAR_DISPLAY
from chip8.servicos.gui import display


def mainloop(contexto: CONTEXTO_RUNTIME):
    clock = pygame.time.Clock()
    rodando = True
    while rodando:
        contexto = obter_decodificar_executar(contexto)
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.display.quit()
                rodando = False
                break

            if (event.type == ID_TIPO_EVENTO_ATUALIZAR_DISPLAY):
                atualizar_display(event)

        clock.tick(60)
        print(clock.get_fps())
