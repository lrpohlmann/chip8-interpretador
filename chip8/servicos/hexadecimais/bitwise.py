from chip8.servicos.inteiros.conversao import inteiros_para_hexadecimais


def hexadecimal_bit_or(hex1: str, hex2: str) -> str:
    int1 = int(hex1, 16)
    int2 = int(hex2, 16)
    or_bit = int1 | int2
    return inteiros_para_hexadecimais(or_bit)


def hexadecimal_bit_and(hex1: str, hex2: str) -> str:
    int1 = int(hex1, 16)
    int2 = int(hex2, 16)
    and_bit = int1 & int2
    return inteiros_para_hexadecimais(and_bit)


def hexadecimal_bit_xor(hex1: str, hex2: str) -> str:
    int1 = int(hex1, 16)
    int2 = int(hex2, 16)
    xor_bit = int1 ^ int2
    return inteiros_para_hexadecimais(xor_bit)


def hexadecimal_bit_right_shift(hex1: str) -> str:
    int1 = int(hex1, 16)
    right_shift_bit = int1 >> 1
    return inteiros_para_hexadecimais(right_shift_bit)


def hexadecimal_bit_left_shift(hex1: str) -> str:
    int1 = int(hex1, 16)
    left_shift_bit = int1 << 1
    return inteiros_para_hexadecimais(left_shift_bit)
