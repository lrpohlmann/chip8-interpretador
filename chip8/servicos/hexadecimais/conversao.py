def hexadecimal_para_binario(num_hex: str) -> str:
    return bin(
        int(
            num_hex, 16
        )
    )
