from chip8.nucleo.dados.tipos import CONTEXTO_RUNTIME
from chip8.nucleo.operacoes.codigo_contexto_runtime import ler_contexto_runtime, escrever_contexto_runtime
from chip8.nucleo.operacoes.codigo_registradores import ler_registrador, escrever_registrador
from chip8.servicos.hexadecimais.aritimetica import subtrair_hexadecimais
from chip8.nucleo.operacoes.execucao.subexecucao.numero_ira_setar_o_vf import numero_ira_setar_o_vf


def escrever_no_registrador_vy_a_subtracao_vy_vx_e_setar_vf(vx: str, vy: str, contexto_runtime: CONTEXTO_RUNTIME) -> CONTEXTO_RUNTIME:
    registradores = ler_contexto_runtime(contexto_runtime, "registradores")

    valor_vy = ler_registrador(registradores, vy)
    valor_vx = ler_registrador(registradores, vx)
    subtracao_vy_vx = subtrair_hexadecimais(valor_vy, valor_vx)

    if numero_ira_setar_o_vf(subtracao_vy_vx):
        valor_final_vy = "0"
        valor_final_vf = "1"
    else:
        valor_final_vy = subtracao_vy_vx
        valor_final_vf = "0"

    registradores_com_subtracao = escrever_registrador(
        registradores, vy, valor_final_vy)
    registradores_com_vf_setado = escrever_registrador(
        registradores_com_subtracao, "f", valor_final_vf)

    return escrever_contexto_runtime(contexto_runtime, "registradores", registradores_com_vf_setado)
