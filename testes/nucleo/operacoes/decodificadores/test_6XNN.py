from chip8.nucleo.operacoes.decodificadores import decoder_6XNN


def test_decoder_6XNN():
    instrucao = "6DFF"
    partial_da_execucao_da_instrucao_set_vx_register_com_endereco_e_dado_preenchido = decoder_6XNN(
        instrucao, lambda endereco_vx, dado: (endereco_vx, dado))
    assert partial_da_execucao_da_instrucao_set_vx_register_com_endereco_e_dado_preenchido.args[
        0] == "D"
    assert partial_da_execucao_da_instrucao_set_vx_register_com_endereco_e_dado_preenchido.args[
        1] == "FF"
