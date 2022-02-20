from pathlib import Path
from typing import Sequence


def _obter_byte_string_da_rom(caminho: Path) -> bytes:
    with open(str(caminho), "rb") as rom:
        bytes_string = rom.readlines()[0]

    return bytes_string


def _fracionar_byte_string_da_rom_em_1_byte(bytes_string: bytes) -> Sequence[str]:
    return bytes_string.hex(":", 1).split(":")


def obter_instrucoes_da_rom(caminho_rom: Path) -> Sequence[str]:
    return _fracionar_byte_string_da_rom_em_1_byte(
        _obter_byte_string_da_rom(caminho_rom)
    )
