from chip8.nucleo.operacoes.decodificadores import decoder_DXYN


def test_decoder_DXYN():
    instrucao = "d01f"
    partial_da_execucao_da_instrucao_draw_sprite_to_screen = decoder_DXYN(
        instrucao, lambda x, y, n: (x, y, n))
    assert partial_da_execucao_da_instrucao_draw_sprite_to_screen.args == (
        "0", "1", "f")
