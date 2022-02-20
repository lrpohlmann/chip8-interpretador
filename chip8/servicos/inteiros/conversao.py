def inteiros_para_hexadecimais(inteiro: int) -> str:
    return hex(inteiro).replace("0x", "", 1)
