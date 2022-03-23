from chip8.nucleo.operacoes.decodificadores._8XY4 import decode_8XY4


def test_decode_8XY4():
    instrucao = "8ab4"

    def teste_assert(vx, vy):
        assert vx == "a"
        assert vy == "b"

    func = decode_8XY4(instrucao, teste_assert)
    func()
