from typing import Callable, Union

from immutables import Map

from chip8.nucleo.dados.tipos import CONTEXTO_RUNTIME

from chip8.nucleo.operacoes.decodificadores._6XNN import decoder_6XNN
from chip8.nucleo.operacoes.decodificadores._7XNN import decoder_7XNN
from chip8.nucleo.operacoes.decodificadores._1NNN import decoder_1NNN
from chip8.nucleo.operacoes.decodificadores._ANNN import decoder_ANNN
from chip8.nucleo.operacoes.decodificadores._DXYN import decoder_DXYN

from chip8.nucleo.operacoes.execucao.jump import _jump
from chip8.nucleo.operacoes.execucao.escrever_no_registrador_vx import _escrever_no_registrador_vx
from chip8.nucleo.operacoes.execucao.somar_no_registrador_vx import _somar_no_registrador_vx
from chip8.nucleo.operacoes.execucao.escrever_no_registrador_index import _escrever_no_registrador_index
from chip8.nucleo.operacoes.execucao.desenhar_na_tela import _desenhar_na_tela
from chip8.nucleo.operacoes.codigo_contexto_runtime import ler_contexto_runtime, escrever_contexto_runtime
from chip8.nucleo.operacoes.execucao.limpar_tela import limpar_tela


def decodificar(contexto_runtime: CONTEXTO_RUNTIME) -> Callable[[CONTEXTO_RUNTIME], CONTEXTO_RUNTIME]:
    instrucao = ler_contexto_runtime(contexto_runtime, "ultima_instrucao")
    if instrucao == "00e0":
        return escrever_contexto_runtime(contexto_runtime, "ultima_execucao", limpar_tela)

    elif instrucao[0] == "1":
        return escrever_contexto_runtime(contexto_runtime, "ultima_execucao", decoder_1NNN(instrucao, _jump))

    elif instrucao[0] == "6":
        return escrever_contexto_runtime(contexto_runtime, "ultima_execucao", decoder_6XNN(instrucao, _escrever_no_registrador_vx))

    elif instrucao[0] == "7":
        return escrever_contexto_runtime(contexto_runtime, "ultima_execucao", decoder_7XNN(instrucao, _somar_no_registrador_vx))

    elif instrucao[0] == "a":
        return escrever_contexto_runtime(contexto_runtime, "ultima_execucao", decoder_ANNN(instrucao, _escrever_no_registrador_index))

    elif instrucao[0] == "d":
        return escrever_contexto_runtime(contexto_runtime, "ultima_execucao", decoder_DXYN(instrucao, _desenhar_na_tela))

    else:
        raise Exception(f"DECODIFICA????O: instru????o {instrucao} desconhecida.")
