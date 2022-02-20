from functools import singledispatch
from operator import add, eq
from typing import Any, Dict, Mapping, Sequence, Tuple, TypeVar, Union

from chip8.nucleo.dados.type_alias import RAM
from chip8.servicos.hexadecimais.algarismo import \
    SEQUENCIA_ALGARISMOS_HEXADECIMAIS
from chip8.servicos.hexadecimais.aritimetica import somar_hexadecimais
from chip8.servicos.inteiros.conversao import inteiros_para_hexadecimais


def ler_memoria_ram(ram: RAM, endereço: Union[str, int]) -> str:
    endereço = _validar_endereco(endereço)

    try:
        dado = ram[endereço]
    except KeyError:
        # TODO: exception nova
        raise Exception("RAM: Endereço inexistente.")

    if dado == None:
        raise Exception("RAM: Endereço vazio")

    return dado


def escrever_na_memoria_ram(ram: RAM, endereco: str, dado: str) -> RAM:
    endereco = _validar_endereco(endereco)

    if (endereco < inteiros_para_hexadecimais(0)) or (endereco > inteiros_para_hexadecimais(4095)):
        raise Exception(f"RAM: Endereço '{endereco}' inexistente.")

    ram[endereco] = dado
    return ram


def obter_instrucao_completa_da_memoria_e_incrementar_contador(ram: RAM, contador: str) -> Tuple[str, str]:
    return add(ler_memoria_ram(ram, contador), ler_memoria_ram(ram, somar_hexadecimais(contador, "1"))), somar_hexadecimais(contador, "2")


def carregar_programa_na_ram(ram: RAM, instrucoes_bytes: Sequence[str]):
    for endereco, dado in tuple(zip(range(512, 4095 + 1), instrucoes_bytes)):
        ram[inteiros_para_hexadecimais(endereco)] = dado

    return ram


@singledispatch
def _validar_endereco(endereco: object) -> str:
    raise Exception(
        f"RAM: formato do endereço '{type(endereco)}' desconhecido.")


@_validar_endereco.register
def _string(endereco: str) -> str:
    for caractere in endereco:
        if caractere not in SEQUENCIA_ALGARISMOS_HEXADECIMAIS:
            raise Exception(
                f"RAM: Caractere '{caractere}' no endereço '{endereco}' não é um algarismo hexadecimal.")

    return endereco


@_validar_endereco.register
def _inteiro(endereco: int) -> str:
    return inteiros_para_hexadecimais(endereco)
