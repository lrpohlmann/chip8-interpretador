from chip8.nucleo.dados.tipos import CONTEXTO_RUNTIME
from chip8.nucleo.operacoes.codigo_contexto_runtime import ler_contexto_runtime, escrever_contexto_runtime
from chip8.nucleo.operacoes.codigo_registradores import ler_registrador, escrever_registrador


def escrever_no_registrador_vx_o_valor_do_registrador_vy(endereco_vx: str, endereco_vy: str, contexto_runtime: CONTEXTO_RUNTIME) -> CONTEXTO_RUNTIME:
    registradores = ler_contexto_runtime(contexto_runtime, "registradores")

    valor_vy = ler_registrador(registradores, endereco_vy)

    registradores_novo_valor_vx = escrever_registrador(
        registradores, endereco_vx, valor_vy)

    return escrever_contexto_runtime(contexto_runtime, "registradores", registradores_novo_valor_vx)
