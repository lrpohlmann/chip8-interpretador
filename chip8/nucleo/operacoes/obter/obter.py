from functools import reduce
from operator import add
from typing import Sequence, Tuple, overload
from chip8.nucleo.dados.instrucao import criar_instrucao
from chip8.nucleo.dados.tipos import CONTADOR, INSTRUCAO_COMPLETA_CHIP8, RAM, e_instrucao
from chip8.nucleo.operacoes.codigo_contador import incrementar_contador_por_dois
from chip8.nucleo.operacoes.codigo_ram import ler_memoria_ram, ler_ram_no_endereco_fornecido_e_nos_enderecos_n_bytes_a_frente
from chip8.servicos.hexadecimais.aritimetica import somar_hexadecimais


def obter_instrucao_completa_da_memoria_e_incrementar_contador(ram: RAM, contador: CONTADOR) -> Tuple[INSTRUCAO_COMPLETA_CHIP8, CONTADOR]:

    dados = ler_ram_no_endereco_fornecido_e_nos_enderecos_n_bytes_a_frente(
        ram, contador, 1)
    instrucao_completa = criar_instrucao(dados)
    contador_incrementado = incrementar_contador_por_dois(contador)

    return instrucao_completa, contador_incrementado
