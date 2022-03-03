from chip8.nucleo.dados.tipos import CONTEXTO_RUNTIME, FUNCOES_EXECUCAO
from chip8.nucleo.operacoes.codigo_contexto_runtime import ler_contexto_runtime


def executar(contexto_runtime: CONTEXTO_RUNTIME) -> CONTEXTO_RUNTIME:
    funcao_a_executar: FUNCOES_EXECUCAO = ler_contexto_runtime(
        contexto_runtime, "ultima_execucao")

    return funcao_a_executar(contexto_runtime)
