from chip8.nucleo.dados.tipos import CONTEXTO_RUNTIME
from chip8.nucleo.operacoes.codigo_contexto_runtime import atualizar_contexto_runtime, ler_contexto_runtime
from chip8.nucleo.operacoes.codigo_registradores import ler_registrador
from chip8.servicos.hexadecimais.aritimetica import somar_hexadecimais


def jump_para_endereco_mais_v0(endereco: str, v0: str, contexto_runtime: CONTEXTO_RUNTIME) -> CONTEXTO_RUNTIME:
    valor_v0 = ler_registrador(ler_contexto_runtime(
        contexto_runtime, "registradores"), v0)
    return atualizar_contexto_runtime(contexto_runtime, "contador", lambda contador: somar_hexadecimais(endereco, valor_v0))
