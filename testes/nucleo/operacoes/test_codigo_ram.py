from operator import eq

from chip8.nucleo.dados.tipos import RAM
from chip8.nucleo.operacoes.codigo_ram import carregar_programa_na_ram, ler_memoria_ram, escrever_na_memoria_ram, obter_instrucao_completa_da_memoria_e_incrementar_contador
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
    ram = escrever_na_memoria_ram(ram, 1, "ff")
    assert ram[inteiros_para_hexadecimais(1)] == "ff"


def test_ler_instrucao(programa, ram_com_programa_carregada: RAM):
    primeira_instrucao = programa[0] + programa[1]
    primeira_instrucao_obtida, primeiro_contador_incrementado = obter_instrucao_completa_da_memoria_e_incrementar_contador(
        ram_com_programa_carregada, "200")

    assert eq(primeira_instrucao_obtida, primeira_instrucao)
    assert eq(primeiro_contador_incrementado, "202")

    segunda_instrucao = programa[2] + programa[3]
    segunda_instrucao_obtida, segundo_contador_incrementado = obter_instrucao_completa_da_memoria_e_incrementar_contador(
        ram_com_programa_carregada, primeiro_contador_incrementado)

    assert eq(segunda_instrucao_obtida, segunda_instrucao)
    assert eq(segundo_contador_incrementado, "204")
