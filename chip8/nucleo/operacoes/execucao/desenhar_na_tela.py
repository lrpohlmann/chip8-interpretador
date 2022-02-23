from chip8.nucleo.dados.type_alias import PIXEL_MAP, RAM, REGISTRADOR_INDEX, REGISTRADORES, SPRITE
from chip8.nucleo.operacoes.codigo_registradores import ler_registrador, ler_registrador_index
from chip8.nucleo.operacoes.codigo_ram import ler_memoria_ram
from chip8.servicos.hexadecimais.conversao import hexadecimal_para_binario
from chip8.servicos.inteiros.conversao import inteiros_para_hexadecimais
from chip8.servicos.binarios.validacao import validar_binario
from chip8.nucleo.operacoes import inserir_sprite_no_pixel_map

from chip8.servicos import log_parametros_e_retorno_da_funcao


@log_parametros_e_retorno_da_funcao
def _desenhar_na_tela(endereco_registrador_x: str, endereco_registrador_y: str, bytes_para_ler_da_memoria_a_partir_do_registrador_index: str, ram: RAM, registradores: REGISTRADORES, registrador_index: REGISTRADOR_INDEX, contador: str, pixel_map: PIXEL_MAP):
    endereco_inicial = int(ler_registrador_index(registrador_index), 16)
    endereco_final = endereco_inicial + int(
        bytes_para_ler_da_memoria_a_partir_do_registrador_index, 16) + 1

    sprite: SPRITE = [validar_binario(hexadecimal_para_binario(
        ler_memoria_ram(ram, inteiros_para_hexadecimais(endereco)))) for endereco in range(endereco_inicial, endereco_final)]

    pixel_map = inserir_sprite_no_pixel_map(
        pixel_map,
        ler_registrador(registradores, endereco_registrador_x),
        ler_registrador(registradores, endereco_registrador_y),
        sprite)

    return {"ram": ram, "registradores": registradores, "registrador_index": registrador_index, "contador": contador, "pixel_map": pixel_map}
