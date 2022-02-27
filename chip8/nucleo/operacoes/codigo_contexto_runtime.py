from typing import Union
from chip8.nucleo.dados import criar_contexto_runtime, e_ram
from chip8.nucleo.dados.tipos import CONTADOR, CONTEXTO_RUNTIME, CONTEXTO_RUNTIME_KEYS, PIXEL_MAP, RAM, REGISTRADOR_INDEX, REGISTRADORES, e_contador, e_pixel_map, e_registrador, e_registrador_index


def ler_contexto_runtime(contexto: CONTEXTO_RUNTIME, chave: CONTEXTO_RUNTIME_KEYS):
    try:
        valor = contexto[chave]
    except KeyError:
        raise Exception(f"CONTEXTO RUNTIME: '{chave}' chave desconhecida")

    if chave == "ram" and e_ram(valor):
        return valor
    elif chave == "registradores" and e_registrador(valor):
        return valor
    elif chave == "registrador_index" and e_registrador_index(valor):
        return valor
    elif chave == "contador" and e_contador(valor):
        return valor
    elif chave == "pixel_map" and e_pixel_map(valor):
        return valor
    else:
        raise Exception()


def escrever_contexto_runtime(contexto: CONTEXTO_RUNTIME, chave: CONTEXTO_RUNTIME_KEYS, valor: Union[RAM, REGISTRADORES, REGISTRADOR_INDEX, CONTADOR, PIXEL_MAP]) -> CONTEXTO_RUNTIME:
    if chave == "ram" and e_ram(valor):
        return contexto.set(chave, valor)
    elif chave == "registradores" and e_registrador(valor):
        return contexto.set(chave, valor)
    elif chave == "registrador_index" and e_registrador_index(valor):
        return contexto.set(chave, valor)
    elif chave == "contador" and e_contador(valor):
        return contexto.set(chave, valor)
    elif chave == "pixel_map" and e_pixel_map(valor):
        return contexto.set(chave, valor)
    else:
        raise Exception()
