from immutables import Map
from chip8.nucleo.dados.tipos import CONTEXTO_RUNTIME, CONTEXTO_RUNTIME_KEYS, e_ram
from chip8.nucleo.dados.ram import criar_memoria_ram
from chip8.nucleo.dados.registradores import criar_registrador_index, criar_registradores
from chip8.nucleo.dados.pixel_map import criar_pixel_map
from chip8.nucleo.dados.contador import criar_contador


def criar_contexto_runtime() -> CONTEXTO_RUNTIME:
    ram = criar_memoria_ram()
    registradores = criar_registradores()
    registrador_index = criar_registrador_index()
    pixel_map = criar_pixel_map()
    contador = criar_contador()

    return Map(  # type: ignore
        ram=ram,
        registradores=registradores,
        registrador_index=registrador_index,
        contador=contador,
        pixel_map=pixel_map
    )
