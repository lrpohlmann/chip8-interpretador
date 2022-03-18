from chip8.nucleo.dados.tipos import CONTEXTO_RUNTIME
from chip8.nucleo.operacoes.codigo_contexto_runtime import ler_contexto_runtime, escrever_contexto_runtime
from chip8.nucleo.operacoes.codigo_registradores import ler_registrador, escrever_registrador
from chip8.servicos.hexadecimais.bitwise import hexadecimal_bit_or


def escrever_no_registrador_vx_o_valor_vx_or_vy(vx: str, vy: str, contexto_runtime: CONTEXTO_RUNTIME) -> CONTEXTO_RUNTIME:
    registradores = ler_contexto_runtime(contexto_runtime, "registradores")

    valor_vx = ler_registrador(registradores, vx)
    valor_vy = ler_registrador(registradores, vy)

    vx_or_vy = hexadecimal_bit_or(valor_vx, valor_vy)

    registradores_escrito = escrever_registrador(registradores, vx, vx_or_vy)

    return escrever_contexto_runtime(contexto_runtime, "registradores", registradores_escrito)
