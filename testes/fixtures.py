from pytest import fixture
from pathlib import Path
from typing import List, Optional, Sequence, Tuple

from chip8.nucleo.dados.tipos import RAM, CONTEXTO_RUNTIME, REGISTRADOR_INDEX, REGISTRADORES, PIXEL_MAP, CONTADOR
from chip8.nucleo.operacoes.codigo_ram import carregar_programa_na_ram
from chip8.nucleo.dados.ram import criar_memoria_ram
from chip8.nucleo.dados.registradores import criar_registrador_index, criar_registradores
from chip8.nucleo.dados.pixel_map import criar_pixel_map
from chip8.nucleo.dados.contexto_runtime import criar_contexto_runtime
from chip8.nucleo.operacoes.codigo_rom import obter_instrucoes_da_rom
from chip8.nucleo.dados.contador import criar_contador

from chip8.nucleo.operacoes.codigo_contexto_runtime import ler_contexto_runtime, escrever_contexto_runtime


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


@fixture
def setup_contexto_runtime():
    def _setup(*, ram: Optional[List[Tuple[str, str]]] = None, registradores: Optional[List[Tuple[str, str]]] = None):
        contexto_runtime = criar_contexto_runtime()
        contexto_runtime = escrever_contexto_runtime(
            contexto_runtime, "ram", _setup_ram(ram))
        contexto_runtime = escrever_contexto_runtime(
            contexto_runtime, "registradores", _setup_registradores(registradores))

        return contexto_runtime

    return _setup


def _setup_ram(chave_valor: Optional[List[Tuple[str, str]]]):
    ram = criar_memoria_ram()
    if chave_valor:
        with ram.mutate() as mutar:
            for chave, valor in chave_valor:
                mutar[chave] = valor

            ram = mutar.finish()  # type: ignore

    return ram


@fixture
def setup_registradores():
    return _setup_registradores


def _setup_registradores(chave_valor: Optional[List[Tuple[str, str]]]):
    registradores = criar_registradores()
    if chave_valor:
        with registradores.mutate() as mutar:
            for chave, valor in chave_valor:
                mutar[chave] = valor

            registradores = mutar.finish()  # type: ignore

    return registradores
