from functools import singledispatch
import re
from typing import Any, Dict, NoReturn, Optional, Union

from chip8.nucleo.dados.tipos import DIGITOS_HEXADECIMAIS, REGISTRADOR_INDEX, REGISTRADORES
from chip8.servicos.hexadecimais.algarismo import SEQUENCIA_ALGARISMOS_HEXADECIMAIS
from chip8.servicos.inteiros.conversao import inteiros_para_hexadecimais


def ler_registrador(registrador: REGISTRADORES, endereco: Union[str, int]) -> str:
    endereco = _validar_endereco(endereco)
    try:
        valor = registrador[endereco]
    except KeyError:
        raise Exception(f"Registradores: {endereco} inexistente.")

    if valor == None:
        raise Exception(f"REGISTRADORES: vazio.")
    elif isinstance(valor, str):
        return valor
    else:
        raise Exception(f"REGISTRADORES: valor '{valor}' desconhecido.")


def escrever_registrador(registrador: REGISTRADORES, endereco: Union[str, int], dado: str) -> REGISTRADORES:
    endereco = _validar_endereco(endereco)

    if not isinstance(dado, str):
        raise Exception("REGISTRADORES: valor '{dado}' não suportado.")

    try:
        registrador[endereco] = dado
        return registrador
    except KeyError:
        raise Exception(f"Registradores: endereço '{endereco}' inexistente.")


def ler_registrador_index(r_index: REGISTRADOR_INDEX) -> str:
    valor = r_index["i"]
    if valor == None:
        raise Exception("REGISTRADOR INDEX: vazio.")
    elif isinstance(valor, str):
        return valor
    else:
        raise Exception(f"REGISTRADOR INDEX: valor '{valor}' desconhecido.")


def escrever_registrador_index(r_index: REGISTRADOR_INDEX, dado: str) -> REGISTRADOR_INDEX:

    if not isinstance(dado, str):
        raise Exception("REGISTRADOR INDEX: valor '{dado}' não suportado.")

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
