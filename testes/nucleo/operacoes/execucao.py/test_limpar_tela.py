from chip8.nucleo.operacoes.execucao.limpar_tela import limpar_tela
from chip8.nucleo.operacoes.codigo_contexto_runtime import escrever_contexto_runtime, ler_contexto_runtime
from testes.fixtures import *


def test_limpar_tela(contexto_runtime, pixel_map_totalmente_preenchido):
    contexto_runtime = escrever_contexto_runtime(
        contexto_runtime, "pixel_map", pixel_map_totalmente_preenchido)

    contexto_runtime_com_tela_limpa = limpar_tela(contexto_runtime)

    assert set(ler_contexto_runtime(
        contexto_runtime_com_tela_limpa,
        "pixel_map").values()
    ) == {0, }
