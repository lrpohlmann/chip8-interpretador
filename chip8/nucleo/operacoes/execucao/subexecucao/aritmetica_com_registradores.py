from typing import Literal
from chip8.nucleo.dados.tipos import REGISTRADORES
from chip8.nucleo.operacoes.execucao.subexecucao.numero_ira_setar_o_vf import numero_ira_setar_o_vf
from chip8.servicos.hexadecimais.aritimetica import somar_hexadecimais, subtrair_hexadecimais
from chip8.nucleo.operacoes.codigo_registradores import ler_registrador, escrever_registrador


def aritimetica_entre_registradores_que_seta_vf(operacao: Literal["soma", "subtracao"], registradores: REGISTRADORES, endereco1: str, endereco2: str) -> REGISTRADORES:
    valor1 = ler_registrador(registradores, endereco1)
    valor2 = ler_registrador(registradores, endereco2)
    resultado = _definir_e_realizar_aritimetica(operacao, valor1, valor2)
    if numero_ira_setar_o_vf(resultado):
        if operacao == "soma":
            numero_a_escrever_no_registrador = "ff"
        else:
            numero_a_escrever_no_registrador = "0"

        valor_vf = "1"
    else:
        numero_a_escrever_no_registrador = resultado
        valor_vf = "0"

    return escrever_registrador(
        escrever_registrador(registradores, endereco1,
                             numero_a_escrever_no_registrador),
        "f",
        valor_vf
    )


def aritimetica_entre_registradores(operacao: Literal["soma", "subtracao"], registradores: REGISTRADORES, endereco1: str, endereco2: str) -> REGISTRADORES:
    valor2 = ler_registrador(registradores, endereco2)
    return aritimetica_entre_registrador_e_numero(operacao, registradores, endereco1, valor2)


def aritimetica_entre_registrador_e_numero(operacao: Literal["soma", "subtracao"], registradores: REGISTRADORES, endereco_registrador: str, numero: str) -> REGISTRADORES:
    valor = ler_registrador(registradores, endereco_registrador)
    resultado = _definir_e_realizar_aritimetica(operacao, valor, numero)

    return escrever_registrador(registradores, endereco_registrador, resultado)


def _definir_e_realizar_aritimetica(operacao, valor, numero) -> str:
    if operacao == "soma":
        resultado = somar_hexadecimais(valor, numero)
    elif operacao == "subtracao":
        resultado = subtrair_hexadecimais(valor, numero)
    else:
        raise Exception()

    return resultado
