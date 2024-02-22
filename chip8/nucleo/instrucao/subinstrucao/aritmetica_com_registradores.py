from typing import Literal
from chip8.nucleo import Registradores, ENDERECO_REGISTRADORES
from chip8.servicos.hexadecimais.aritimetica import (
    somar_hexadecimais,
    subtrair_hexadecimais,
)


def aritimetica_entre_registradores_que_seta_vf(
    operacao: Literal["soma", "subtracao"],
    registradores: Registradores,
    endereco1: ENDERECO_REGISTRADORES,
    endereco2: ENDERECO_REGISTRADORES,
) -> Registradores:
    valor1 = registradores[endereco1]
    valor2 = registradores[endereco2]
    resultado = _definir_e_realizar_aritimetica(operacao, valor1, valor2)
    num_int = int(resultado, 16)
    if num_int > 255 or num_int < 0:
        if operacao == "soma":
            numero_a_escrever_no_registrador = "ff"
        else:
            numero_a_escrever_no_registrador = "0"

        valor_vf = "1"
    else:
        numero_a_escrever_no_registrador = resultado
        valor_vf = "0"

    registradores[endereco1] = numero_a_escrever_no_registrador
    registradores["f"] = valor_vf
    return registradores


def aritimetica_entre_registrador_e_numero(
    operacao: Literal["soma", "subtracao"],
    registradores: Registradores,
    endereco_registrador: ENDERECO_REGISTRADORES,
    numero: str,
) -> Registradores:
    valor = registradores[endereco_registrador]
    resultado = _definir_e_realizar_aritimetica(operacao, valor, numero)

    registradores[endereco_registrador] = resultado
    return registradores


def _definir_e_realizar_aritimetica(operacao, valor, numero) -> str:
    if operacao == "soma":
        resultado = somar_hexadecimais(valor, numero)
    elif operacao == "subtracao":
        resultado = subtrair_hexadecimais(valor, numero)
    else:
        raise Exception()

    return resultado
