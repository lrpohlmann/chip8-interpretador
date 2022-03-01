from pathlib import Path
from typing import Sequence

from chip8.nucleo.dados.tipos import SEQUENCIA_INSTRUCOES_CHIP8_FRACIONADAS_EM_2BYTES


def _obter_byte_string_da_rom(caminho: Path) -> bytes:
    with open(str(caminho), "rb") as rom:
        bytes_string = rom.readlines()[0]

    return bytes_string


def _fracionar_byte_string_da_rom_em_1_byte(bytes_string: bytes) -> SEQUENCIA_INSTRUCOES_CHIP8_FRACIONADAS_EM_2BYTES:
    return bytes_string.hex(":", 1).split(":")


def obter_instrucoes_da_rom(caminho_rom: Path) -> SEQUENCIA_INSTRUCOES_CHIP8_FRACIONADAS_EM_2BYTES:
    return _fracionar_byte_string_da_rom_em_1_byte(
        _obter_byte_string_da_rom(caminho_rom)
    )
