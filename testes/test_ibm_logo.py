from pathlib import Path
import logging
import os
from chip8.nucleo.dados.ram import criar_memoria_ram
from chip8.nucleo.dados.registradores import criar_registradores, criar_registrador_index
from chip8.nucleo.operacoes.codigo_rom import obter_instrucoes_da_rom
from chip8.nucleo.operacoes.codigo_ram import carregar_programa_na_ram, obter_instrucao_completa_da_memoria_e_incrementar_contador
from chip8.nucleo.dados.pixel_map import criar_pixel_map
from chip8.app.decodificar import decodificar
from chip8.nucleo.operacoes.type_alias import CONTEXTO_RUNTIME


def ibm():
    contexto: CONTEXTO_RUNTIME = {
        "ram": criar_memoria_ram(),
        "registradores": criar_registradores(),
        "registrador_index": criar_registrador_index(),
        "contador": "200",
        "pixel_map": criar_pixel_map()}

    instrucoes = obter_instrucoes_da_rom(Path("rom/IBM Logo.ch8"))
    contexto["ram"] = carregar_programa_na_ram(contexto["ram"], instrucoes)
    while True:
        instrucao, contador = obter_instrucao_completa_da_memoria_e_incrementar_contador(
            contexto["ram"], contexto["contador"])

        contexto["contador"] = contador

        if len(contexto["registrador_index"].keys()) > 1:
            print("i")

        if instrucao[0] == "d":
            print(instrucao)
        execucao = decodificar(instrucao)
        if execucao:
            contexto = execucao(**contexto)


if __name__ == "__main__":
    flnm = Path.cwd() / "log.log"
    if flnm.exists():
        os.remove(str(flnm))

    logging.basicConfig(filename=str(
        Path.cwd() / "log.log"), level=logging.DEBUG)
    ibm()
