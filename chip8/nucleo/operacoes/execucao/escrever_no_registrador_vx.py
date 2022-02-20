from typing import Dict

from chip8.nucleo.dados.type_alias import RAM, REGISTRADOR_INDEX, REGISTRADORES
from chip8.nucleo.operacoes.type_alias import RETORNO_FUNCOES_EXECUCAO
from chip8.nucleo.operacoes.codigo_registradores import escrever_registrador

from chip8.servicos import log_parametros_e_retorno_da_funcao


@log_parametros_e_retorno_da_funcao
def _escrever_no_registrador_vx(endereco_registrador: str, dado: str, ram: RAM, registradores: REGISTRADORES, registrador_index: REGISTRADOR_INDEX, contador: str) -> RETORNO_FUNCOES_EXECUCAO:
    registradores_escrito = escrever_registrador(
        registradores, endereco_registrador, dado)
    return ram, registradores_escrito, registrador_index, contador
