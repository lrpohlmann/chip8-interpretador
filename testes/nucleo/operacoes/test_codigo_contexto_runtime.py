from chip8.nucleo.operacoes.codigo_contexto_runtime import (
    atualizar_contexto_runtime, atualizar_varios_valores_contexto_runtime, escrever_contexto_runtime, escrever_varios_valores_contexto_runtime, ler_contexto_runtime)
from chip8.nucleo.operacoes.codigo_registradores import escrever_registrador
from testes.fixtures import *


def test_ler_contexto_runtime(contexto_runtime: CONTEXTO_RUNTIME):
    ler_contexto_runtime(contexto_runtime, "ram")
    ler_contexto_runtime(contexto_runtime, "registradores")
    ler_contexto_runtime(contexto_runtime, "registrador_index")
    ler_contexto_runtime(contexto_runtime, "contador")
    ler_contexto_runtime(contexto_runtime, "pixel_map")


def test_falha_ler_contexto_runtime(contexto_runtime):
    try:
        ler_contexto_runtime(contexto_runtime, "1111")
        assert False
    except Exception as e:
        assert True


def test_escrever_runtime(contexto_runtime: CONTEXTO_RUNTIME):
    nova_ram = criar_memoria_ram()
    novo_registradores = criar_registradores()
    novo_registrador_index = criar_registrador_index()
    novo_contador = criar_contador()
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


def test_falha_escrever_contexto_runtime(contexto_runtime):
    try:
        escrever_contexto_runtime(contexto_runtime, "ram", "a")
        assert False
    except Exception as e:
        assert True


def test_escrever_varios_valores_contexto_runtime(contexto_runtime):

    ram = criar_memoria_ram().set("0", "1")
    contador = "300"

    relacao_chave_valor = {
        "ram": ram,
        "contador": contador
    }

    novo_contexto = escrever_varios_valores_contexto_runtime(
        contexto_runtime, relacao_chave_valor)

    assert novo_contexto["ram"] == ram
    assert novo_contexto["contador"] == contador


def test_atualizar_contexto_runtime(contexto_runtime):

    contexto_atualizado = atualizar_contexto_runtime(
        contexto_runtime, "registradores", lambda x: escrever_registrador(x, "0", "1"))
    assert contexto_atualizado["registradores"]["0"] == "1"


def test_atualizar_varios_valores_contexto_runtime(contexto_runtime):
    relacao_chave_atualizar_func = {
        "registradores": lambda reg: escrever_registrador(reg, "0", "1"),
        "contador": lambda cont: "300",
    }

    contexto_atualizado = atualizar_varios_valores_contexto_runtime(
        contexto_runtime, relacao_chave_atualizar_func)
    assert contexto_atualizado["registradores"]["0"] == "1"
    assert contexto_atualizado["contador"] == "300"
