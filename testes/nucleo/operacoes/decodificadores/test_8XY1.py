from chip8.nucleo.operacoes.decodificadores._8XY1 import decoder_8XY1


def test_decoder_8XY1():
    instrucao = "8011"

    def teste_assert(vx, vy):
        assert vx == "0"
        assert vy == "1"

    exec_func = decoder_8XY1(instrucao, teste_assert)
    exec_func()
