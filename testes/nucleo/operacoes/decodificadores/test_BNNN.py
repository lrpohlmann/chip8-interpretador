from chip8.nucleo.operacoes.decodificadores._BNNN import decode_BNNN


def test_decode_BNNN():
    instrucao = "b200"

    def test_assert(endereco):
        assert endereco == "200"

    func = decode_BNNN(instrucao, test_assert)
    func()
