from chip8.nucleo.operacoes.decodificadores._8XY3 import decode_8XY3
from testes.fixtures import setup_contexto_runtime


def test_decode_8XY3(setup_contexto_runtime):
    instrucao = "8013"

    def teste_assert(vx, vy):
        assert vx == "0"
        assert vy == "1"

    func = decode_8XY3(instrucao, teste_assert)
    func()
