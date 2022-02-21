from chip8.nucleo.operacoes.decodificadores import decoder_1NNN


def test_decoder_1NNN():
    instrucao = "1200"
    partial_da_execucao_da_instrucao_jump_com_endereco_preenchido = decoder_1NNN(
        instrucao, lambda endereco: endereco)
    assert partial_da_execucao_da_instrucao_jump_com_endereco_preenchido.args[0] == "200"
