from chip8.nucleo.instrucao import jump_1NNN
from testes.fixtures import *


def test_jump(contexto_runtime):
    jump_1NNN("1300")(contexto_runtime)
    assert contexto_runtime.contador == "300"
