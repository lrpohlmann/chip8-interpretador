from chip8.nucleo.dados.tipos import CONTEXTO_RUNTIME
from chip8.nucleo.operacoes.codigo_registradores import ler_registrador, escrever_registrador
from chip8.nucleo.operacoes.codigo_contexto_runtime import ler_contexto_runtime, escrever_contexto_runtime
from chip8.servicos.hexadecimais.bitwise import hexadecimal_bit_xor


def escrever_no_registrador_vx_o_valor_vx_xor_vy(vx: str, vy: str, contexto_runtime: CONTEXTO_RUNTIME) -> CONTEXTO_RUNTIME:
    registradores = ler_contexto_runtime(contexto_runtime, "registradores")

    valor_vx = ler_registrador(registradores, vx)
    valor_vy = ler_registrador(registradores, vy)
    valor_vx_xor_vy = hexadecimal_bit_xor(valor_vx, valor_vy)
    registradores_atualizados = escrever_registrador(
        registradores, vx, valor_vx_xor_vy)

    return escrever_contexto_runtime(contexto_runtime, "registradores", registradores_atualizados)
