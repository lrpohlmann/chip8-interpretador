from chip8.nucleo.dados.tipos import CONTEXTO_RUNTIME
from chip8.nucleo.operacoes.codigo_contexto_runtime import atualizar_contexto_runtime
from chip8.nucleo.operacoes.codigo_pixel_map import zerar_pixel_map


def limpar_tela(contexto_runtime: CONTEXTO_RUNTIME):
    return atualizar_contexto_runtime(contexto_runtime, "pixel_map", zerar_pixel_map)
