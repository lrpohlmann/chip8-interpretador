from chip8.nucleo.operacoes.execucao import _jump
from testes.fixtures import *


def test_jump(contexto_runtime):
    retorno = _jump("300", contexto_runtime)
    assert retorno["contador"] == "300"
