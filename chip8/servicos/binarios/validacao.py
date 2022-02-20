from operator import eq


def _remover_0b(bin_str: str) -> str:
    if eq(bin_str[0:2], "0b"):
        return bin_str[2:]

    return bin_str


def _completar_binario_com_zeros_para_formar_byte(bin_str: str) -> str:
    return bin_str.zfill(8)


def validar_binario(bin_str: str) -> str:
    return _completar_binario_com_zeros_para_formar_byte(
        _remover_0b(
            bin_str
        )
    )
