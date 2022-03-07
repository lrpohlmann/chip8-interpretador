from typing import Tuple
from chip8.nucleo.dados.instrucao import criar_instrucao
from chip8.nucleo.dados.tipos import CONTEXTO_RUNTIME, INSTRUCAO_COMPLETA_CHIP8
from chip8.nucleo.operacoes.codigo_contador import incrementar_contador_por_dois
from chip8.nucleo.operacoes.codigo_ram import ler_ram_no_endereco_fornecido_e_nos_enderecos_n_bytes_a_frente
from chip8.nucleo.operacoes.codigo_contexto_runtime import ler_contexto_runtime, escrever_contexto_runtime


def obter(contexto_runtime: CONTEXTO_RUNTIME) -> CONTEXTO_RUNTIME:
    ram = ler_contexto_runtime(contexto_runtime, "ram")
    contador = ler_contexto_runtime(contexto_runtime, "contador")

    dados = ler_ram_no_endereco_fornecido_e_nos_enderecos_n_bytes_a_frente(
        ram, contador, 1)
    instrucao_completa = criar_instrucao(dados)
    contador_incrementado = incrementar_contador_por_dois(contador)

    novo_contexto = escrever_contexto_runtime(
        contexto_runtime, "contador", contador_incrementado)

    novo_contexto = escrever_contexto_runtime(
        novo_contexto, "ultima_instrucao", instrucao_completa
    )

    return novo_contexto
