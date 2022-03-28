from chip8.nucleo.dados.tipos import CONTEXTO_RUNTIME
from chip8.nucleo.operacoes.codigo_contexto_runtime import ler_contexto_runtime, escrever_contexto_runtime, atualizar_contexto_runtime
from chip8.nucleo.operacoes.codigo_registradores import escrever_registrador, ler_registrador
from chip8.nucleo.operacoes.execucao.subexecucao.aritmetica_com_registradores import aritimetica_entre_registradores_que_seta_vf
from chip8.servicos.hexadecimais.aritimetica import somar_hexadecimais
from chip8.nucleo.operacoes.execucao.subexecucao.numero_ira_setar_o_vf import numero_ira_setar_o_vf


def escrever_no_registrador_vx_a_soma_vx_e_vy_e_setar_vf(vx: str, vy: str, contexto_runtime: CONTEXTO_RUNTIME) -> CONTEXTO_RUNTIME:
    return atualizar_contexto_runtime(contexto_runtime, "registradores",
                                      lambda reg: aritimetica_entre_registradores_que_seta_vf("soma", reg, vx, vy))
