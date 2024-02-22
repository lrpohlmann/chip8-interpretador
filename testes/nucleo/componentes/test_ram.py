import pytest

from chip8.nucleo.componentes.ram import Ram


def test_criacao_ram():
    ram = Ram()

    assert max(ram._ram.keys()) == "fff"


def test_leitura_vazio():
    ram = Ram()
    with pytest.raises(Exception):
        ram["0"]


def test_leitura_e_acesso_normal():
    ram = Ram()
    ram["f"] = "ff"
    assert ram["f"] == "ff"


def test_leitura_endereco_inexistente():
    ram = Ram()
    with pytest.raises(Exception):
        v = ram["h"]
