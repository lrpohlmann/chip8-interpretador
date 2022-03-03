from pathlib import Path
import logging
import os
from time import sleep

from chip8.nucleo.dados.ram import criar_memoria_ram
from chip8.nucleo.dados.registradores import criar_registradores, criar_registrador_index
from chip8.nucleo.operacoes.codigo_rom import obter_instrucoes_da_rom
from chip8.nucleo.operacoes.codigo_ram import carregar_programa_na_ram
from chip8.nucleo.operacoes.obter.obter import obter_instrucao_completa_da_memoria_e_incrementar_contador
from chip8.nucleo.dados.pixel_map import criar_pixel_map
from chip8.nucleo.dados.contexto_runtime import criar_contexto_runtime
from chip8.nucleo.operacoes.codigo_contexto_runtime import ler_contexto_runtime, escrever_contexto_runtime
from chip8.nucleo.operacoes.decodificadores.decodificar import decodificar
from chip8.nucleo.operacoes.execucao.execucao import executar
from chip8.nucleo.dados.tipos import CONTEXTO_RUNTIME
from chip8.servicos import display


def ibm():

    display.setup_tela()

    contexto = criar_contexto_runtime()

    instrucoes = obter_instrucoes_da_rom(Path("rom/IBM Logo.ch8"))
    ram_carregada = carregar_programa_na_ram(
        ler_contexto_runtime(contexto, "ram"), instrucoes)

    contexto = escrever_contexto_runtime(contexto, "ram", ram_carregada)

    while True:
        sleep(0.1)
        contexto = obter_instrucao_completa_da_memoria_e_incrementar_contador(
            contexto)

        contexto = decodificar(contexto)
        contexto = executar(contexto)


if __name__ == "__main__":
    flnm = Path.cwd() / "log.log"
    if flnm.exists():
        os.remove(str(flnm))

    logging.basicConfig(filename=str(
        Path.cwd() / "log.log"), level=logging.DEBUG)
    ibm()
