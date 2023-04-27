from chip8.servicos import map
from chip8.nucleo.operacoes.execucao import _desenhar_na_tela
from chip8.nucleo.operacoes import (
    escrever_na_memoria_ram,
    escrever_registrador_index,
    escrever_registrador,
)
from chip8.nucleo.operacoes.codigo_contexto_runtime import (
    escrever_contexto_runtime,
    ler_contexto_runtime,
)
from testes.fixtures import *


def test_desenhar_na_tela(contexto_runtime: CONTEXTO_RUNTIME):
    mutacao = contexto_runtime.evolver()
    mutacao["registrador_index"] = escrever_registrador_index(
        contexto_runtime.get("registrador_index"), "200"
    )

    ram = contexto_runtime.get("ram")
    with ram.mutate() as mutar_ram:
        mutar_ram["200"] = "ff"
        mutar_ram["201"] = "ff"
        mutar_ram["202"] = "ff"
        mutar_ram["203"] = "ff"
        mutar_ram["204"] = "ff"
        mutar_ram["205"] = "ff"
        mutar_ram["206"] = "ff"
        mutar_ram["207"] = "ff"
        mutar_ram["208"] = "ff"
        mutar_ram["209"] = "ff"
        mutar_ram["20a"] = "ff"
        mutar_ram["20b"] = "ff"
        mutar_ram["20c"] = "ff"
        mutar_ram["20d"] = "ff"
        mutar_ram["20e"] = "ff"
        ram = mutar_ram.finish()
    mutacao["ram"] = ram

    registradores = contexto_runtime.get("registradores")
    with registradores.mutate() as mutar_registradores:
        mutar_registradores["0"] = "0"
        mutar_registradores["1"] = "0"
        registradores = mutar_registradores.finish()

    mutacao["registradores"] = registradores

    novo_contexto = mutacao.persistent()

    resultado = _desenhar_na_tela("0", "1", "f", novo_contexto)

    for x in range(0, 8):
        for y in range(0, 15):
            assert resultado["pixel_map"][(x, y)] == 1
            mutar_pixel = resultado["pixel_map"].evolver()
            mutar_pixel.remove((x, y))
            resultado = escrever_contexto_runtime(
                resultado, "pixel_map", mutar_pixel.persistent()
            )

    for i in resultado["pixel_map"].values():
        assert i == 0

    assert resultado["registradores"]["f"] == "0"


def test_registrador_f_set(contexto_runtime: CONTEXTO_RUNTIME):
    mutacao = contexto_runtime.evolver()
    mutacao["registrador_index"] = escrever_registrador_index(
        contexto_runtime.get("registrador_index"), "200"
    )

    ram = contexto_runtime.get("ram")
    with ram.mutate() as mutar_ram:
        mutar_ram["200"] = "ff"
        ram = mutar_ram.finish()
    mutacao["ram"] = ram

    mutar_pixel = {}
    for n in range(0, 8):
        mutar_pixel[(n, 0)] = 1
    mutacao["pixel_map"] = map.atualizar(contexto_runtime.get("pixel_map"), mutar_pixel)

    registradores = contexto_runtime.get("registradores")
    with registradores.mutate() as mutar_registradores:
        mutar_registradores["0"] = "0"
        mutar_registradores["1"] = "0"
        registradores = mutar_registradores.finish()

    mutacao["registradores"] = registradores

    novo_contexto = mutacao.persistent()

    resultado = _desenhar_na_tela("0", "1", "1", novo_contexto)

    assert resultado["registradores"]["f"] == "1"
