from immutables import Map
from pytest import fixture
from pathlib import Path
from typing import Dict, Sequence

from chip8.nucleo import *
from chip8.nucleo.operacoes.codigo_ram import carregar_programa_na_ram
from chip8.nucleo.operacoes.codigo_rom import obter_instrucoes_da_rom
from chip8.nucleo.dados.contador import criar_contador


@fixture
def ram():
    return criar_memoria_ram()


@fixture
def contador():
    return criar_contador()


@fixture
def programa():
    return obter_instrucoes_da_rom(Path("rom/IBM Logo.ch8"))


@fixture
def ram_com_programa_carregada(ram: RAM, programa: Sequence[str]):
    return carregar_programa_na_ram(ram, programa)


@fixture
def registradores():
    return criar_registradores()


@fixture
def registrador_index():
    return criar_registrador_index()


@fixture
def pixel_map():
    return criar_pixel_map()


@fixture
def pixel_map_totalmente_preenchido(pixel_map):
    with pixel_map.mutate() as mutar:
        for coord in pixel_map.keys():
            mutar[coord] = 1

        return mutar.finish()


@fixture
def contexto_runtime():
    return criar_contexto_runtime()
