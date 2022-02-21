from chip8.nucleo.operacoes.codigo_ram import (
    carregar_programa_na_ram, escrever_na_memoria_ram, ler_memoria_ram,
    obter_instrucao_completa_da_memoria_e_incrementar_contador)
from chip8.nucleo.operacoes.codigo_registradores import (
    escrever_registrador, escrever_registrador_index, ler_registrador,
    ler_registrador_index)
from chip8.nucleo.operacoes.codigo_rom import obter_instrucoes_da_rom
from chip8.nucleo.operacoes.type_alias import FUNCOES_EXECUCAO, RAM, REGISTRADOR_INDEX, REGISTRADORES, RETORNO_FUNCOES_EXECUCAO
