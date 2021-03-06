from functools import singledispatch
from operator import add
from typing import Final, Sequence, Tuple, Union

from chip8.nucleo.dados.tipos import CONTADOR, DIGITOS_HEXADECIMAIS, INSTRUCAO_COMPLETA_CHIP8, RAM, e_instrucao, e_ram
from chip8.servicos.hexadecimais.algarismo import \
    SEQUENCIA_ALGARISMOS_HEXADECIMAIS
from chip8.servicos.hexadecimais.aritimetica import somar_hexadecimais
from chip8.servicos.inteiros.conversao import inteiros_para_hexadecimais
from chip8.servicos.hexadecimais.conversao import hexadecimal_para_inteiro
from chip8.nucleo.operacoes.codigo_contador import incrementar_contador_por_dois


def ler_memoria_ram(ram: RAM, endereço: Union[str, int]) -> str:
    endereço = _validar_endereco(endereço)

    try:
        dado = ram[endereço]
    except KeyError:
        # TODO: exception nova
        raise Exception("RAM: Endereço inexistente.")

    if dado == None:
        raise Exception(f"RAM: Endereço '{endereço}' vazio.")
    elif isinstance(dado, str):
        return dado
    else:
        raise Exception(f"RAM: Dado '{dado}' desconhecido.")


def escrever_na_memoria_ram(ram: RAM, endereco: str, dado: str) -> RAM:
    endereco = _validar_endereco(endereco)

    if (endereco < inteiros_para_hexadecimais(0)) or (endereco > inteiros_para_hexadecimais(4095)):
        raise Exception(f"RAM: Endereço '{endereco}' inexistente.")

    ram_escrita = ram.set(endereco, dado)
    if e_ram(ram_escrita):
        return ram_escrita
    else:
        raise Exception()


def carregar_programa_na_ram(ram: RAM, instrucoes_bytes: Sequence[str]) -> RAM:
    ENDERECO_INICIO_INSTRUCOES: Final = 512  # hexadecimal: 200
    ENDERECO_MAXIMO_RAM: Final = 4095
    AGRUPAMENTO_ENDERECO_MEIA_INSTRUCAO: Final = tuple(
        zip(range(ENDERECO_INICIO_INSTRUCOES, ENDERECO_MAXIMO_RAM + 1), instrucoes_bytes))

    for endereco, meia_instrucao in AGRUPAMENTO_ENDERECO_MEIA_INSTRUCAO:
        ram = escrever_na_memoria_ram(
            ram,
            inteiros_para_hexadecimais(endereco),
            meia_instrucao
        )

    return ram


def ler_ram_no_endereco_fornecido_e_nos_enderecos_n_bytes_a_frente(ram: RAM, endereco: str, n_bytes: int) -> Sequence[str]:
    return [
        ler_memoria_ram(
            ram,
            somar_hexadecimais(
                endereco,
                inteiros_para_hexadecimais(b)
            )
        )
        for b in range(0, n_bytes + 1)
    ]


@ singledispatch
def _validar_endereco(endereco: object) -> str:
    raise Exception(
        f"RAM: formato do endereço '{type(endereco)}' desconhecido.")


@ _validar_endereco.register
def _string(endereco: str) -> str:
    for caractere in endereco:
        if caractere not in SEQUENCIA_ALGARISMOS_HEXADECIMAIS:
            raise Exception(
                f"RAM: Caractere '{caractere}' no endereço '{endereco}' não é um algarismo hexadecimal.")

    return endereco


@ _validar_endereco.register
def _inteiro(endereco: int) -> str:
    return inteiros_para_hexadecimais(endereco)
