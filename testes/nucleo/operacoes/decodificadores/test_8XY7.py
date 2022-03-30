from chip8.nucleo.operacoes.decodificadores._8XY7 import decode_8XY7


def test_decode_8XY7():
    instrucao = "8017"

    def test_assert(vx, vy):
        assert vx == instrucao[1]
        assert vy == instrucao[2]

    func = decode_8XY7(instrucao, test_assert)
    func()
