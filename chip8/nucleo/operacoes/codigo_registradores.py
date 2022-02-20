from functools import singledispatch
from typing import Any, Dict, NoReturn, Union

from chip8.nucleo.dados.type_alias import DIGITOS_HEXADECIMAIS, REGISTRADOR_INDEX, REGISTRADORES
from chip8.servicos.hexadecimais.algarismo import SEQUENCIA_ALGARISMOS_HEXADECIMAIS
from chip8.servicos.inteiros.conversao import inteiros_para_hexadecimais


def ler_registrador(registrador: REGISTRADORES, endereco: Union[str, int]) -> str:
    endereco = _validar_endereco(endereco)
    try:
        return registrador[endereco]
    except KeyError:
        raise Exception(f"Registradores: {endereco} inexistente.")


def escrever_registrador(registrador: REGISTRADORES, endereco: Union[str, int], dado: str) -> REGISTRADORES:
    endereco = _validar_endereco(endereco)
    try:
        registrador[endereco] = dado
        return registrador
    except KeyError:
        raise Exception(f"Registradores: endereço '{endereco}' inexistente.")


def ler_registrador_index(r_index: REGISTRADOR_INDEX) -> str:
    return r_index["i"]


def escrever_registrador_index(r_index: REGISTRADOR_INDEX, dado: str) -> REGISTRADOR_INDEX:
    r_index["i"] = dado
    return r_index


# TODO: duplicado da RAM
@singledispatch
def _validar_endereco(endereco: object) -> str:
    raise Exception(
        f"REGISTRADORES: formato do endereço '{type(endereco)}' desconhecido.")


@_validar_endereco.register
def _string(endereco: str) -> str:
    for caractere in endereco:
        if caractere not in SEQUENCIA_ALGARISMOS_HEXADECIMAIS:
            raise Exception(
                f"REGISTRADORES: Caractere '{caractere}' no endereço '{endereco}' não é um algarismo hexadecimal.")

    return endereco


@_validar_endereco.register
def _inteiro(endereco: int) -> str:
    return inteiros_para_hexadecimais(endereco)
