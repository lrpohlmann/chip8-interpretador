from chip8.nucleo.operacoes.decodificadores import decoder_ANNN


def test_decoder_ANNN():
    instrucao = "a777"
    partial_da_execucao_da_instrucao_add_value_to_vx_com_endereco_preenchido = decoder_ANNN(
        instrucao, lambda i: i)
    assert partial_da_execucao_da_instrucao_add_value_to_vx_com_endereco_preenchido.args[
        0] == '777'
