from functools import reduce, singledispatch
from typing import Mapping, Union

from chip8.nucleo.dados.tipos import REGISTRADOR_INDEX, REGISTRADORES, e_registrador, e_registrador_index
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

    if endereco not in registrador.keys():
        raise Exception(f"Registradores: endereço '{endereco}' inexistente.")

    registrador_escrito = registrador.set(endereco, dado)
    if e_registrador(registrador_escrito):
        return registrador_escrito
    else:
        raise Exception()


def escrever_varios_valores_registrador(registrador, par_endereco_valor: Mapping[str, str]) -> REGISTRADORES:
    registrador_novo = reduce(lambda reg, endereco_valor: escrever_registrador(
        reg, endereco_valor[0], endereco_valor[1]), par_endereco_valor.items(), registrador)
    return registrador_novo


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

    r_index_escrito = r_index.set("i", dado)
    if e_registrador_index(r_index_escrito):
        return r_index_escrito
    else:
        raise Exception()


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
