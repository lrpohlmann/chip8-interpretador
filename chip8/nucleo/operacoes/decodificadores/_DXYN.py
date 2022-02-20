from functools import partial


def decoder_DXYN(instrucao, func):
    vx = instrucao[1]
    vy = instrucao[2]
    bytes_para_ler = instrucao[3]
    return partial(func, vx, vy, bytes_para_ler)
