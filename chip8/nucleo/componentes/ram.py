from chip8.servicos.inteiros.conversao import inteiros_para_hexadecimais


class Ram:
    def __init__(self, tamanho=4096) -> None:
        self._ram: dict[str, str | None] = {
            inteiros_para_hexadecimais(n): None for n in range(0, tamanho)
        }

    def __setitem__(self, __key: str | int, __value: str) -> None:
        if isinstance(__key, int):
            __key = inteiros_para_hexadecimais(__key)

        if __key not in self._ram:
            raise Exception(f"RAM: Endereço {__key} desconhecido.")

        self._ram[__key] = __value

    def __getitem__(self, __key: str | int) -> str:
        if isinstance(__key, int):
            __key = inteiros_para_hexadecimais(__key)

        if __key not in self._ram:
            raise Exception(f"RAM: Endereço {__key} desconhecido.")

        valor = self._ram[__key]
        if valor is None:
            raise Exception(f"RAM: Enredeço {__key} vazio.")

        return valor

    def __str__(self) -> str:
        return self._ram.__str__()

    def __repr__(self) -> str:
        return self._ram.__repr__()
