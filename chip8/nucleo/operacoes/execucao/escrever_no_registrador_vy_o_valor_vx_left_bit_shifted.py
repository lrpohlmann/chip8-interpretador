from chip8.nucleo.dados.tipos import CONTEXTO_RUNTIME
from chip8.nucleo.operacoes.codigo_contexto_runtime import atualizar_contexto_runtime
from chip8.nucleo.operacoes.execucao.subexecucao.bitwise_shift_registradores import bitwise_shift_registradores


def escrever_no_registrador_vy_o_valor_vx_left_bit_shifted(vx: str, vy: str, contexto_runtime: CONTEXTO_RUNTIME) -> CONTEXTO_RUNTIME:
    return atualizar_contexto_runtime(contexto_runtime, "registradores", lambda reg: bitwise_shift_registradores(reg, vx, vy, "left"))
