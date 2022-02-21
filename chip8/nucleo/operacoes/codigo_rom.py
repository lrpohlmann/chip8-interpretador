from pathlib import Path
from typing import Sequence

from chip8.nucleo.dados.type_alias import INSTRUCOES_CHIP8


def _obter_byte_string_da_rom(caminho: Path) -> bytes:
    with open(str(caminho), "rb") as rom:
        bytes_string = rom.readlines()[0]

    return bytes_string


def _fracionar_byte_string_da_rom_em_1_byte(bytes_string: bytes) -> INSTRUCOES_CHIP8:
    return bytes_string.hex(":", 1).split(":")


def obter_instrucoes_da_rom(caminho_rom: Path) -> INSTRUCOES_CHIP8:
    return _fracionar_byte_string_da_rom_em_1_byte(
        _obter_byte_string_da_rom(caminho_rom)
    )
