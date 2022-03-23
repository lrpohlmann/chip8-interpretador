from chip8.nucleo.dados.tipos import CONTEXTO_RUNTIME
from chip8.nucleo.operacoes.codigo_contexto_runtime import ler_contexto_runtime, escrever_contexto_runtime
from chip8.nucleo.operacoes.codigo_registradores import escrever_registrador, ler_registrador
from chip8.servicos.hexadecimais.aritimetica import somar_hexadecimais
from chip8.nucleo.operacoes.execucao.subexecucao.numero_ira_setar_o_vf import numero_ira_setar_o_vf


def escrever_no_registrador_vx_a_soma_vx_e_vy_e_setar_vf(vx: str, vy: str, contexto_runtime: CONTEXTO_RUNTIME) -> CONTEXTO_RUNTIME:
    registradores = ler_contexto_runtime(contexto_runtime, "registradores")

    valor_vx = ler_registrador(registradores, vx)
    valor_vy = ler_registrador(registradores, vy)
    valor_soma_vx_vy = somar_hexadecimais(valor_vx, valor_vy)

    if numero_ira_setar_o_vf(valor_soma_vx_vy):
        registradores_vx_somado = escrever_registrador(registradores, vx, "ff")
        registradores_vf_setado = escrever_registrador(
            registradores_vx_somado, "f", "1")
        return escrever_contexto_runtime(contexto_runtime, "registradores", registradores_vf_setado)
    else:
        registradores_vx_somado = escrever_registrador(
            registradores, vx, valor_soma_vx_vy)
        registradores_vf_nao_setado = escrever_registrador(
            registradores_vx_somado, "f", "0")
        return escrever_contexto_runtime(contexto_runtime, "registradores", registradores_vf_nao_setado)
