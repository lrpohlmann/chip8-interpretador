from chip8.nucleo.operacoes.decodificadores._8XY0 import decoder_8XY0
from chip8.nucleo.operacoes.codigo_contexto_runtime import ler_contexto_runtime, escrever_contexto_runtime


def test_decoder_8XY0():
    instrucao = "8010"

    def _assert_func(vx, vy):
        assert vx == instrucao[1]
        assert vy == instrucao[2]

    exec_func = decoder_8XY0(instrucao, _assert_func)
    exec_func()
