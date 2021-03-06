from operator import eq

from chip8.nucleo.dados.tipos import RAM
from chip8.nucleo.operacoes.codigo_ram import carregar_programa_na_ram, ler_memoria_ram, escrever_na_memoria_ram, ler_ram_no_endereco_fornecido_e_nos_enderecos_n_bytes_a_frente
from chip8.nucleo.operacoes.obter.obter import obter
from chip8.servicos.inteiros.conversao import inteiros_para_hexadecimais
from testes.fixtures import *


def test_ler_ram(ram: RAM):
    dado = "ff"
    ram = ram.set(inteiros_para_hexadecimais(1), dado)
    dado_lido_da_ram_com_hexadecimal = ler_memoria_ram(
        ram, inteiros_para_hexadecimais(1))
    assert eq(dado_lido_da_ram_com_hexadecimal, dado)

    dado_lido_da_ram_com_inteiro = ler_memoria_ram(ram, 1)
    assert eq(dado_lido_da_ram_com_inteiro, dado)


def test_carregar_programa(ram: RAM, programa):
    ram_carregada = carregar_programa_na_ram(ram, programa)
    for endereco in range(512, 512 + len(programa)):
        assert eq(
            type(ram_carregada[inteiros_para_hexadecimais(endereco)]), str)

    for endereco_vazio in list(list(range(0, 512)) + list(range(512 + len(programa), 4095))):
        assert eq(
            ram_carregada[inteiros_para_hexadecimais(endereco_vazio)], None)


def test_escrever_memoria_ram(ram: RAM):
    ram = escrever_na_memoria_ram(ram, "1", "ff")
    assert ram["1"] == "ff"


def test_ler_a_frente_memoria_ram(ram: RAM):
    with ram.mutate() as setup_ram:
        setup_ram["0"] = "ff"
        setup_ram["1"] = "aa"
        setup_ram["2"] = "11"
        ram = setup_ram.finish()

    resultado = ler_ram_no_endereco_fornecido_e_nos_enderecos_n_bytes_a_frente(
        ram, "0", 2)
    assert resultado == ["ff", "aa", "11"]
