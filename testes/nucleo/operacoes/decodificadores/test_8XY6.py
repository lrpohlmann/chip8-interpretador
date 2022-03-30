from chip8.nucleo.operacoes.decodificadores._8XY6 import decode_8XY6


def test_decode_8XY6():
    instrucao = "8af6"

    def test_assert(vx, vy):
        assert vx == instrucao[1]
        assert vy == instrucao[2]

    func = decode_8XY6(instrucao, test_assert)
    func()
