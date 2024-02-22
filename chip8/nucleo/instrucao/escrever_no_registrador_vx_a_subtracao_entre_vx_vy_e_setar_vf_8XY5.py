from chip8.nucleo.instrucao.subinstrucao.aritmetica_com_registradores import (
    aritimetica_entre_registradores_que_seta_vf,
)
from chip8.nucleo import ContextoRuntime


def escrever_no_registrador_vx_a_subtracao_entre_vx_vy_e_setar_vf_8XY5(
    instrucao: str, contexto_runtime: ContextoRuntime
) -> ContextoRuntime:
    vx = instrucao[1]
    vy = instrucao[2]
    contexto_runtime.registradores = aritimetica_entre_registradores_que_seta_vf(
        "subtracao", contexto_runtime.registradores, vx, vy
    )
    return contexto_runtime
