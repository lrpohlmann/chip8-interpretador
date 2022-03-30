from chip8.nucleo.operacoes.codigo_contexto_runtime import atualizar_contexto_runtime
from chip8.nucleo.operacoes.execucao.subexecucao.aritmetica_com_registradores import aritimetica_entre_registradores_que_seta_vf
from chip8.nucleo.dados.tipos import CONTEXTO_RUNTIME


def escrever_no_registrador_vx_a_subtracao_entre_vx_vy_e_setar_vf(vx: str, vy: str, contexto_runtime: CONTEXTO_RUNTIME) -> CONTEXTO_RUNTIME:
    return atualizar_contexto_runtime(contexto_runtime, "registradores", lambda reg: aritimetica_entre_registradores_que_seta_vf("subtracao", reg, vx, vy))
