from chip8.servicos.hexadecimais.conversao import hexadecimal_para_inteiro
from chip8.servicos.inteiros.conversao import inteiros_para_hexadecimais


def hexadecimal_bit_or(hex1: str, hex2: str) -> str:
    int1 = hexadecimal_para_inteiro(hex1)
    int2 = hexadecimal_para_inteiro(hex2)
    or_bit = int1 | int2
    return inteiros_para_hexadecimais(or_bit)


def hexadecimal_bit_and(hex1: str, hex2: str) -> str:
    int1 = hexadecimal_para_inteiro(hex1)
    int2 = hexadecimal_para_inteiro(hex2)
    and_bit = int1 & int2
    return inteiros_para_hexadecimais(and_bit)


def hexadecimal_bit_xor(hex1: str, hex2: str) -> str:
    int1 = hexadecimal_para_inteiro(hex1)
    int2 = hexadecimal_para_inteiro(hex2)
    xor_bit = int1 ^ int2
    return inteiros_para_hexadecimais(xor_bit)
