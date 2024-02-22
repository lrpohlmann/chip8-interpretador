from testes.fixtures import *
from chip8.nucleo.instrucao import (
    escrever_no_registrador_index_ANNN,
)


def test_escrever_no_registrador_index(contexto_runtime):
    escrever_no_registrador_index_ANNN("a300")(contexto_runtime)
    assert contexto_runtime.registradores.i == "300"
