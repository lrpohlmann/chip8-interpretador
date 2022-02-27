from immutables import Map
from pytest import fixture
from pathlib import Path
from typing import Dict, Sequence

from chip8.nucleo import *
from chip8.nucleo.operacoes.codigo_ram import carregar_programa_na_ram
from chip8.nucleo.operacoes.codigo_rom import obter_instrucoes_da_rom


@fixture
def ram():
    return criar_memoria_ram()


@fixture
def programa():
    return obter_instrucoes_da_rom(Path("rom/IBM Logo.ch8"))


@fixture
def ram_com_programa_carregada(ram: Dict, programa: Sequence[str]):
    return carregar_programa_na_ram(ram, programa)


@fixture
def registradores():
    return criar_registradores()


@fixture
def registrador_index():
    return {"i": None}


@fixture
def pixel_map():
    return criar_pixel_map()


@fixture
def contexto_runtime():
    return Map(**{
        "ram": criar_memoria_ram(),
        "registradores": criar_registradores(),
        "registrador_index": criar_registrador_index(),
        "contador": "200",
        "pixel_map": criar_pixel_map()
    })
