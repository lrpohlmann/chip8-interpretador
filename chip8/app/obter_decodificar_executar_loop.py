from functools import reduce
from chip8.nucleo.dados.tipos import CONTEXTO_RUNTIME
from chip8.nucleo.operacoes.decodificadores.decodificar import decodificar
from chip8.nucleo.operacoes.execucao.execucao import executar
from chip8.nucleo.operacoes.obter.obter import obter


def obter_decodificar_executar(contexto: CONTEXTO_RUNTIME) -> CONTEXTO_RUNTIME:
    contexto = reduce(lambda ctx, operacao: operacao(ctx),
                      [
        obter,
        decodificar,
        executar
    ], contexto)

    return contexto
