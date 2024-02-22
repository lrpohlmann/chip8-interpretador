from chip8.nucleo.instrucao import limpar_tela_00e0
from testes.fixtures import *


def test_limpar_tela(contexto_runtime):
    contexto_runtime.tela.desenhar_sprite(["11111111"], "0", "0")

    limpar_tela_00e0(contexto_runtime)

    assert set(contexto_runtime.tela._pixels.values()) == {
        0,
    }
