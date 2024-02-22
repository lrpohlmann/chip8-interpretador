from chip8.nucleo.componentes import Tela


def test_tela():
    tela = Tela()
    tela.desenhar_sprite(["11111111", "11111111"], "0", "0")
    for n in range(0, 8):
        assert tela[(n, 0)] == 1
        assert tela[(n, 1)] == 1

    assert not tela.pixel_mudou_1_para_0

    tela.desenhar_sprite(["11111111", "11111111"], "0", "0")
    for n in range(0, 8):
        assert tela[(n, 0)] == 0
        assert tela[(n, 1)] == 0

    assert tela.pixel_mudou_1_para_0
