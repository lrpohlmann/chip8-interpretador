def hexadecimal_para_binario(num_hex: str) -> str:
    return bin(
        int(
            num_hex, 16
        )
    ).replace("0b", "", 1).replace("-", "", 1)


def hexadecimal_para_inteiro(num_hex: str) -> int:
    return int(
        num_hex, 16
    )
