from typing import Literal
from chip8.nucleo.instrucao import desenhar_na_tela_DXYN
from chip8.nucleo.componentes import ContextoRuntime
from testes.fixtures import *


def _(i, dado):
    i["i"] = dado
    return i


def test_desenhar_na_tela(contexto_runtime: ContextoRuntime):
    contexto_runtime.registradores.i = "200"

    contexto_runtime.ram["200"] = "ff"
    contexto_runtime.ram["201"] = "ff"
    contexto_runtime.ram["202"] = "ff"
    contexto_runtime.ram["203"] = "ff"
    contexto_runtime.ram["204"] = "ff"
    contexto_runtime.ram["205"] = "ff"
    contexto_runtime.ram["206"] = "ff"
    contexto_runtime.ram["207"] = "ff"
    contexto_runtime.ram["208"] = "ff"
    contexto_runtime.ram["209"] = "ff"
    contexto_runtime.ram["20a"] = "ff"
    contexto_runtime.ram["20b"] = "ff"
    contexto_runtime.ram["20c"] = "ff"
    contexto_runtime.ram["20d"] = "ff"
    contexto_runtime.ram["20e"] = "ff"

    contexto_runtime.registradores["0"] = "0"
    contexto_runtime.registradores["1"] = "0"

    desenhar_na_tela_DXYN("d01f")(contexto_runtime)

    for x in range(0, 8):
        for y in range(0, 15):
            assert contexto_runtime.tela[(x, y)] == 1
            contexto_runtime.tela._pixels.pop((x, y))

    for i in contexto_runtime.tela._pixels.values():
        assert i == 0

    assert contexto_runtime.registradores["f"] == "0"


def test_registrador_f_set(contexto_runtime: ContextoRuntime):
    contexto_runtime.ram["200"] = "ff"
    contexto_runtime.registradores.i = "200"

    mutar_pixel: dict[tuple[int, int], Literal[0, 1]] = {}
    for n in range(0, 8):
        mutar_pixel[(n, 0)] = 1

    contexto_runtime.tela._pixels.update(mutar_pixel)

    contexto_runtime.registradores["0"] = "0"
    contexto_runtime.registradores["1"] = "0"

    desenhar_na_tela_DXYN("d011")(contexto_runtime)

    assert contexto_runtime.registradores["f"] == "1"
