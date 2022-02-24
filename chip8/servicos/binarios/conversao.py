def binario_para_hexadecimal(num_bin: str) -> str:
    return hex(
        int(
            num_bin, 2
        )
    ).replace("0x", "", 1)
