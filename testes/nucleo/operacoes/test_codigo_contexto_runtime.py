from chip8.nucleo.operacoes.codigo_contexto_runtime import (
    escrever_contexto_runtime, ler_contexto_runtime)
from testes.fixtures import *


def test_ler_contexto_runtime(contexto_runtime: CONTEXTO_RUNTIME):
    ler_contexto_runtime(contexto_runtime, "ram")
    ler_contexto_runtime(contexto_runtime, "registradores")
    ler_contexto_runtime(contexto_runtime, "registrador_index")
    ler_contexto_runtime(contexto_runtime, "contador")
    ler_contexto_runtime(contexto_runtime, "pixel_map")


def test_escrever_runtime(contexto_runtime: CONTEXTO_RUNTIME):
    nova_ram = criar_memoria_ram()
    novo_registradores = criar_registradores()
    novo_registrador_index = criar_registrador_index()
    novo_contador = "200"
    novo_pixel_map = criar_pixel_map()
    escrever_contexto_runtime(contexto_runtime, "ram", nova_ram)
    escrever_contexto_runtime(
        contexto_runtime, "registradores", novo_registradores)
    escrever_contexto_runtime(
        contexto_runtime, "registrador_index", novo_registrador_index)
    escrever_contexto_runtime(contexto_runtime, "contador", novo_contador)
    escrever_contexto_runtime(contexto_runtime, "pixel_map", novo_pixel_map)

    assert contexto_runtime["ram"] == nova_ram
    assert contexto_runtime["registradores"] == novo_registradores
    assert contexto_runtime["registrador_index"] == novo_registrador_index
    assert contexto_runtime["contador"] == novo_contador
    assert contexto_runtime["pixel_map"] == novo_pixel_map
