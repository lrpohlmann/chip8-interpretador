from functools import partial

from chip8.nucleo import ContextoRuntime, ENDERECO_REGISTRADORES
from chip8.servicos.hexadecimais.bitwise import hexadecimal_bit_xor


def escrever_no_registrador_vx_o_valor_vx_xor_vy_8XY3(instrucao: str):
    vx = instrucao[1]
    vy = instrucao[2]
    return partial(_escrever_no_registrador_vx_o_valor_vx_xor_vy, vx, vy)


def _escrever_no_registrador_vx_o_valor_vx_xor_vy(
    vx: ENDERECO_REGISTRADORES,
    vy: ENDERECO_REGISTRADORES,
    contexto_runtime: ContextoRuntime,
) -> ContextoRuntime:
    val_vx = contexto_runtime.registradores[vx]
    val_vy = contexto_runtime.registradores[vy]
    contexto_runtime.registradores[vx] = hexadecimal_bit_xor(val_vx, val_vy)
    return contexto_runtime
