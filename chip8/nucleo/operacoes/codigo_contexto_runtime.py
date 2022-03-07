from typing import Union
from chip8.nucleo.dados import e_ram
from chip8.nucleo.dados.tipos import CONTADOR, CONTEXTO_RUNTIME, CONTEXTO_RUNTIME_KEYS, INSTRUCAO_COMPLETA_CHIP8, PIXEL_MAP, RAM, REGISTRADOR_INDEX, REGISTRADORES, e_contador, e_instrucao, e_pixel_map, e_registrador, e_registrador_index


def ler_contexto_runtime(contexto: CONTEXTO_RUNTIME, chave: CONTEXTO_RUNTIME_KEYS):
    try:
        valor = contexto[chave]
        return valor
    except KeyError:
        raise Exception(f"CONTEXTO RUNTIME: '{chave}' chave desconhecida")


def escrever_contexto_runtime(contexto: CONTEXTO_RUNTIME, chave: CONTEXTO_RUNTIME_KEYS, valor: Union[RAM, REGISTRADORES, REGISTRADOR_INDEX, CONTADOR, PIXEL_MAP, INSTRUCAO_COMPLETA_CHIP8]) -> CONTEXTO_RUNTIME:
    key_typeguard = {
        "ram": e_ram,
        "registradores": e_registrador,
        "registrador_index": e_registrador_index,
        "contador": e_contador,
        "pixel_map": e_pixel_map,
        "ultima_instrucao": e_instrucao,
        "ultima_execucao": lambda x: True
    }

    try:
        t_guard = key_typeguard[chave]
        if t_guard(valor):
            return contexto.set(chave, valor)

        else:
            raise Exception(
                f"CONTEXTO RUNTIME: valor '{valor}' não é válido para a chave '{chave}'")
    except KeyError:
        raise Exception(f"CONTEXTO RUNTIME: chave '{chave}' inexistente.")
