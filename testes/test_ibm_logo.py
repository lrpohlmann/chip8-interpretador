from pathlib import Path
import logging
import os
from chip8.nucleo.dados.ram import criar_memoria_ram
from chip8.nucleo.dados.registradores import criar_registradores, criar_registrador_index
from chip8.nucleo.operacoes.codigo_rom import obter_instrucoes_da_rom
from chip8.nucleo.operacoes.codigo_ram import carregar_programa_na_ram, obter_instrucao_completa_da_memoria_e_incrementar_contador
from chip8.app.decodificar import decodificar


def ibm():
    ram = criar_memoria_ram()
    registrador = criar_registradores()
    index = criar_registrador_index()
    contador = "200"

    instrucoes = obter_instrucoes_da_rom(Path("rom/IBM Logo.ch8"))
    ram = carregar_programa_na_ram(ram, instrucoes)
    while True:
        instrucao, contador = obter_instrucao_completa_da_memoria_e_incrementar_contador(
            ram, contador)
        if instrucao[0] == "d":
            print(instrucao)
        execucao = decodificar(instrucao)
        if execucao:
            ram, registrador, index, contador = execucao(
                ram, registrador, index, contador)


if __name__ == "__main__":
    flnm = Path.cwd() / "log.log"
    if flnm.exists():
        os.remove(str(flnm))

    logging.basicConfig(filename=str(
        Path.cwd() / "log.log"), level=logging.DEBUG)
    ibm()
