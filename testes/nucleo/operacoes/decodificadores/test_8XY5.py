from chip8.nucleo.operacoes.decodificadores._8XY5 import decode_8XY5


def test_decode_8XY5():
    instrucao = "8015"

    def test_assert(vx, vy):
        assert vx == instrucao[1]
        assert vy == instrucao[2]

    func = decode_8XY5(instrucao, test_assert)
    func()
