from testes.fixtures import *
from chip8.nucleo.operacoes.codigo_contador import incrementar_contador_por_dois, incrementar_contador_por_um


def test_incrementar_contador(contador):
    assert incrementar_contador_por_um(contador) == "201"
    assert incrementar_contador_por_dois(contador) == "202"
