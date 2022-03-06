from typing import Sequence
import pygame

from immutables import Map
from chip8.nucleo.dados.tipos import PIXEL_MAP, SPRITE, CONTEXTO_RUNTIME
from chip8.nucleo.operacoes.codigo_contexto_runtime import escrever_contexto_runtime, ler_contexto_runtime
from chip8.nucleo.operacoes.codigo_registradores import ler_registrador, ler_registrador_index
from chip8.nucleo.operacoes.codigo_ram import ler_memoria_ram
from chip8.servicos.hexadecimais.conversao import hexadecimal_para_binario, hexadecimal_para_inteiro
from chip8.servicos.inteiros.conversao import inteiros_para_hexadecimais
from chip8.servicos.binarios.validacao import validar_binario
from chip8.servicos.gui import display
from chip8.nucleo.operacoes import inserir_sprite_no_pixel_map
from chip8.servicos.gui.eventos import emitir_evento_atualizar_display

from chip8.servicos import log_parametros_e_retorno_da_funcao


@log_parametros_e_retorno_da_funcao
def _desenhar_na_tela(endereco_registrador_x: str, endereco_registrador_y: str, bytes_para_ler_da_memoria_a_partir_do_registrador_index: str, contexto_runtime: CONTEXTO_RUNTIME) -> CONTEXTO_RUNTIME:
    registradores = ler_contexto_runtime(contexto_runtime, "registradores")
    registrador_index = ler_contexto_runtime(
        contexto_runtime, "registrador_index")
    pixel_map = ler_contexto_runtime(contexto_runtime, "pixel_map")

    endereco_inicial, endereco_final = _calcular_endereco_inicial_e_final_do_sprite_na_memoria_ram(
        bytes_para_ler_da_memoria_a_partir_do_registrador_index, registrador_index)

    sprite = _formar_sprite(contexto_runtime, endereco_inicial, endereco_final)

    pixel_map_desenhado = _produzir_pixel_map(
        endereco_registrador_x, endereco_registrador_y, registradores, pixel_map, sprite)

    pixel_map_diferenca = _diferenca_pixel_map_novo_e_velho(
        pixel_map_desenhado, pixel_map)

    emitir_evento_atualizar_display(pixel_map_diferenca)

    return escrever_contexto_runtime(contexto_runtime, "pixel_map", pixel_map_desenhado)


def _formar_sprite(contexto_runtime, endereco_inicial, endereco_final):
    dados_hexadecimais_para_formar_sprite = [ler_memoria_ram(
        ler_contexto_runtime(contexto_runtime, "ram"),
        inteiros_para_hexadecimais(endereco)) for endereco in range(endereco_inicial, endereco_final)]

    sprite: SPRITE = _tornar_binario_dados_hexadecimais_para_formar_sprite(
        dados_hexadecimais_para_formar_sprite)

    return sprite


def _tornar_binario_dados_hexadecimais_para_formar_sprite(dados: Sequence[str]) -> SPRITE:
    dados_binarios = [hexadecimal_para_binario(x) for x in dados]
    validado = [validar_binario(x) for x in dados_binarios]
    return validado


def _produzir_pixel_map(endereco_registrador_x, endereco_registrador_y, registradores, pixel_map, sprite):
    pixel_map_desenhado = inserir_sprite_no_pixel_map(
        pixel_map,
        ler_registrador(registradores, endereco_registrador_x),
        ler_registrador(registradores, endereco_registrador_y),
        sprite)

    return pixel_map_desenhado


def _calcular_endereco_inicial_e_final_do_sprite_na_memoria_ram(bytes_para_ler_da_memoria_a_partir_do_registrador_index, registrador_index):
    endereco_inicial = hexadecimal_para_inteiro(
        ler_registrador_index(registrador_index))
    endereco_final = endereco_inicial + hexadecimal_para_inteiro(
        bytes_para_ler_da_memoria_a_partir_do_registrador_index)

    return endereco_inicial, endereco_final


def _diferenca_pixel_map_novo_e_velho(novo: PIXEL_MAP, velho: PIXEL_MAP) -> PIXEL_MAP:
    differenca = set(novo.items()) - set(velho.items())
    with Map().mutate() as mut:
        for k, v in differenca:
            mut[k] = v

        pixel_map_diferenca = mut.finish()

    return pixel_map_diferenca
