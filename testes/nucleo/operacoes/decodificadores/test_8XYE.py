from chip8.nucleo.operacoes.decodificadores._8XYE import decode_8XYE


def test_decode_8XYE():
    instrucao = "8d1e"

    def test_assert(vx, vy):
        assert vx == instrucao[1]
        assert vy == instrucao[2]

    func = decode_8XYE(instrucao, test_assert)
    func()
