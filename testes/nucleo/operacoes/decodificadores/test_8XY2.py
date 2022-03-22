from chip8.nucleo.operacoes.decodificadores._8XY2 import decoder_8XY2


def test_decoder_8XY2():
    instrucao = "8012"

    def test_assert(vx, vy):
        assert vx == instrucao[1]
        assert vy == instrucao[2]

    func = decoder_8XY2(instrucao, test_assert)
    func()
