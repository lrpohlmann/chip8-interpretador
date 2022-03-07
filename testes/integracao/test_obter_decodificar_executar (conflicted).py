from immutables import Map
from chip8.nucleo.operacoes.codigo_ram import escrever_na_memoria_ram
from chip8.nucleo.operacoes.obter.obter import obter

from chip8.nucleo.operacoes.codigo_contexto_runtime import escrever_contexto_runtime, ler_contexto_runtime
from chip8.nucleo.operacoes.decodificadores.decodificar import decodificar
from chip8.nucleo.dados.tipos import CONTEXTO_RUNTIME
from testes.fixtures import *


def test_obter_decodificar_executar_6XNN(contexto_runtime: CONTEXTO_RUNTIME):
    contexto_runtime = escrever_contexto_runtime(
        contexto_runtime,
        "ram",
        escrever_na_memoria_ram(ler_contexto_runtime(
            contexto_runtime, "ram"), "200", "60")
    )
    contexto_runtime = escrever_contexto_runtime(
        contexto_runtime,
        "ram",
        escrever_na_memoria_ram(ler_contexto_runtime(
            contexto_runtime, "ram"), "201", "ff")
    )

    contexto_runtime_com_contador_atualizado = obter(
        contexto_runtime)

    contexto_runtime_com_funcao_a_executar = decodificar(
        contexto_runtime_com_contador_atualizado)

    contexto_runtime_atualizado = ler_contexto_runtime(contexto_runtime_com_funcao_a_executar, "ultima_execucao")(
        contexto_runtime_com_funcao_a_executar)

    assert ler_contexto_runtime(
        contexto_runtime_atualizado, "registradores")["0"] == "ff"
    assert contexto_runtime_atualizado["registrador_index"] == Map(i=None)
    assert contexto_runtime_atualizado["contador"] == "202"
