from chip8.nucleo.dados.tipos import CONTEXTO_RUNTIME
from chip8.nucleo.operacoes.codigo_contexto_runtime import escrever_contexto_runtime, ler_contexto_runtime
from chip8.nucleo.operacoes.codigo_pixel_map import zerar_pixel_map


def limpar_tela(contexto_runtime: CONTEXTO_RUNTIME):
    pixel_map = ler_contexto_runtime(contexto_runtime, "pixel_map")
    pixel_map_limpo = zerar_pixel_map(pixel_map)
    contexto_runtime_atualizado = escrever_contexto_runtime(
        contexto_runtime, "pixel_map", pixel_map_limpo)
    return contexto_runtime_atualizado
