from pathlib import Path
from chip8.nucleo import obter_instrucoes_da_rom


def test_obtencao_instrucoes():
    instrucoes = obter_instrucoes_da_rom(
        Path(__file__).parent.parent.parent.parent / "rom/IBM Logo.ch8")
    assert all([len(i) == 2 for i in instrucoes])
