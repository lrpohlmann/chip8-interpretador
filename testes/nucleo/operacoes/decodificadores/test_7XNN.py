from chip8.nucleo.operacoes.decodificadores import decoder_7XNN


def test_decoder_7XNN():
    instrucao = "7a11"
    partial_da_execucao_da_instrucao_add_value_to_vx_com_endereco_preenchido = decoder_7XNN(
        instrucao, lambda vx, valor: (vx, valor))
    assert partial_da_execucao_da_instrucao_add_value_to_vx_com_endereco_preenchido.args[
        0] == "a"
    assert partial_da_execucao_da_instrucao_add_value_to_vx_com_endereco_preenchido.args[
        1] == "11"
