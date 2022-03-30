from typing import Literal

from chip8.nucleo.dados.tipos import REGISTRADORES
from chip8.nucleo.operacoes.codigo_registradores import escrever_registrador, escrever_varios_valores_registrador, ler_registrador
from chip8.servicos.hexadecimais.conversao import hexadecimal_para_binario
from chip8.servicos.hexadecimais.bitwise import hexadecimal_bit_left_shift, hexadecimal_bit_right_shift


def bitwise_shift_registradores(registradores: REGISTRADORES, endereco_valor_a_ser_shifted: str, endereco_onde_salvar_valor_shifted: str, tipo_shift: Literal["left", "right"]) -> REGISTRADORES:
    valor_a_ser_shifted = ler_registrador(
        registradores, endereco_valor_a_ser_shifted)
    if tipo_shift == "left":
        bit_a_salvar_no_vf = _obter_bit_mais_a_esquerda(valor_a_ser_shifted)
        valor_bit_shifted = hexadecimal_bit_left_shift(valor_a_ser_shifted)
    elif tipo_shift == "right":
        bit_a_salvar_no_vf = _obter_bit_mais_a_direita(valor_a_ser_shifted)
        valor_bit_shifted = hexadecimal_bit_right_shift(valor_a_ser_shifted)
    else:
        raise Exception()

    return escrever_varios_valores_registrador(registradores, {endereco_onde_salvar_valor_shifted: valor_bit_shifted, "f": bit_a_salvar_no_vf})


def _obter_bit_mais_a_esquerda(hex_num: str) -> str:
    bits = hexadecimal_para_binario(hex_num)
    bit_mais_a_esquerda = bits[0]
    return bit_mais_a_esquerda


def _obter_bit_mais_a_direita(hex_num: str) -> str:
    bits = hexadecimal_para_binario(hex_num)
    bit_mais_a_direita = bits[-1]
    return bit_mais_a_direita
