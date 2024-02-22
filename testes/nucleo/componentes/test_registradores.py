import pytest

from chip8.nucleo import Registradores


def test_escrita_e_leitura_registradores():
    reg = Registradores()
    reg["0"] = "aa"
    assert reg["0"] == "aa"


def test_leitura_e_escrita_endereco_inexistente():
    reg = Registradores()
    with pytest.raises(Exception):
        reg["l"]

    with pytest.raises(Exception):
        reg["p"] = "10"


def test_leitura_endereco_vazio():
    reg = Registradores()
    with pytest.raises(Exception):
        reg["0"]
