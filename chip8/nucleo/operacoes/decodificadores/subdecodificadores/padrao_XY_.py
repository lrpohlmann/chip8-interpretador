from chip8.nucleo.dados.tipos import INSTRUCAO_COMPLETA_CHIP8


def padrao_xy_(instrucao: INSTRUCAO_COMPLETA_CHIP8):
    vx = instrucao[1]
    vy = instrucao[2]
    return vx, vy
