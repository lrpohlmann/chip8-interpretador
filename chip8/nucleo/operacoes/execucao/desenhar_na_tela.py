from chip8.nucleo.dados.type_alias import RAM, REGISTRADOR_INDEX, REGISTRADORES
from chip8.nucleo.operacoes.codigo_registradores import ler_registrador, ler_registrador_index
from chip8.nucleo.operacoes.codigo_ram import ler_memoria_ram
from chip8.servicos.hexadecimais.conversao import hexadecimal_para_binario
from chip8.servicos.binarios.validacao import validar_binario

from chip8.servicos import log_parametros_e_retorno_da_funcao


@log_parametros_e_retorno_da_funcao
def _desenhar_na_tela(endereco_registrador_x: str, endereco_registrador_y: str, bytes_para_ler_da_memoria_a_partir_do_registrador_index: str, ram: RAM, registradores: REGISTRADORES, registrador_index: REGISTRADOR_INDEX, contador: str):
    endereco_inicial = int(ler_registrador_index(registrador_index), 16)
    endereco_final = endereco_inicial + int(
        bytes_para_ler_da_memoria_a_partir_do_registrador_index, 16) + 1

    sprite = [validar_binario(hexadecimal_para_binario(
        ler_memoria_ram(ram, hex(endereco)))) for endereco in range(endereco_inicial, endereco_final)]

    return ram, registradores, registrador_index, contador
