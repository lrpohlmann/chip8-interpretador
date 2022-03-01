from chip8.nucleo.operacoes.codigo_ram import (
    carregar_programa_na_ram, escrever_na_memoria_ram, ler_memoria_ram)
from chip8.nucleo.operacoes.codigo_registradores import (
    escrever_registrador, escrever_registrador_index, ler_registrador,
    ler_registrador_index)
from chip8.nucleo.operacoes.codigo_rom import obter_instrucoes_da_rom
from chip8.nucleo.operacoes.codigo_pixel_map import inserir_sprite_no_pixel_map
