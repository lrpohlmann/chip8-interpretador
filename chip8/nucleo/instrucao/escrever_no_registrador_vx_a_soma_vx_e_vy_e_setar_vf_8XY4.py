from chip8.nucleo.componentes import ContextoRuntime
from chip8.nucleo.instrucao.subinstrucao.aritmetica_com_registradores import (
    aritimetica_entre_registradores_que_seta_vf,
)


def escrever_no_registrador_vx_a_soma_vx_e_vy_e_setar_vf_8XY4(
    instrucao: str, contexto_runtime: ContextoRuntime
) -> ContextoRuntime:
    vx = instrucao[1]
    vy = instrucao[2]
    contexto_runtime.registradores = aritimetica_entre_registradores_que_seta_vf(
        "soma", contexto_runtime.registradores, vx, vy
    )
    return contexto_runtime
