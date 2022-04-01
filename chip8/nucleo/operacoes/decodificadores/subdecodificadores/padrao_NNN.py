from chip8.nucleo.dados.tipos import INSTRUCAO_COMPLETA_CHIP8


def padrao_NNN(instrucao: INSTRUCAO_COMPLETA_CHIP8) -> str:
    return instrucao[1:]
