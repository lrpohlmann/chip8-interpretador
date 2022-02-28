from chip8.nucleo.operacoes.execucao import _desenhar_na_tela
from chip8.nucleo.operacoes import escrever_na_memoria_ram, escrever_registrador_index, escrever_registrador
from testes.fixtures import *


def test_desenhar_na_tela(contexto_runtime: CONTEXTO_RUNTIME):
    with contexto_runtime.mutate() as mutacao:
        mutacao["registrador_index"] = escrever_registrador_index(
            contexto_runtime.get("registrador_index"), "200")

        ram = contexto_runtime.get("ram")
        with ram.mutate() as mutar_ram:
            mutar_ram["200"] = "ff"
            mutar_ram["201"] = "ff"
            mutar_ram["202"] = "ff"
            ram = mutar_ram.finish()
        mutacao["ram"] = ram

        registradores = contexto_runtime.get("registradores")
        with registradores.mutate() as mutar_registradores:
            mutar_registradores["0"] = "0"
            mutar_registradores["1"] = "0"
            registradores = mutar_registradores.finish()

        mutacao["registradores"] = registradores

        novo_contexto = mutacao.finish()

    resultado = _desenhar_na_tela("0", "1", "2", novo_contexto)

    for x in range(0, 8):
        for y in range(0, 3):
            assert resultado["pixel_map"][(x, y)] == 1
            resultado["pixel_map"].pop((x, y))

    for i in resultado["pixel_map"].values():
        assert i == 0
