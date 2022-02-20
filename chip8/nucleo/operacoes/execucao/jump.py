from typing import Dict

from chip8.nucleo.operacoes.type_alias import RETORNO_FUNCOES_EXECUCAO
from chip8.nucleo.dados.type_alias import RAM, REGISTRADOR_INDEX, REGISTRADORES
from chip8.servicos import log_parametros_e_retorno_da_funcao


@log_parametros_e_retorno_da_funcao
def _jump(pular_para: str, ram: RAM, registradores: REGISTRADORES, registrador_index: REGISTRADOR_INDEX, contador: str) -> RETORNO_FUNCOES_EXECUCAO:
    contador = pular_para
    return ram, registradores, registrador_index, contador
