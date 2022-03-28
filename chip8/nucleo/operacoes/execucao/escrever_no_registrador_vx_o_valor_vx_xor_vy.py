from chip8.nucleo.dados.tipos import CONTEXTO_RUNTIME
from chip8.nucleo.operacoes.codigo_registradores import ler_registrador, escrever_registrador
from chip8.nucleo.operacoes.codigo_contexto_runtime import atualizar_contexto_runtime, ler_contexto_runtime, escrever_contexto_runtime
from chip8.servicos.hexadecimais.bitwise import hexadecimal_bit_xor


def escrever_no_registrador_vx_o_valor_vx_xor_vy(vx: str, vy: str, contexto_runtime: CONTEXTO_RUNTIME) -> CONTEXTO_RUNTIME:
    return atualizar_contexto_runtime(
        contexto_runtime,
        "registradores",
        lambda reg: escrever_registrador(
            reg, vx, hexadecimal_bit_xor(
                ler_registrador(reg, vx), ler_registrador(reg, vy)
            )
        )
    )
