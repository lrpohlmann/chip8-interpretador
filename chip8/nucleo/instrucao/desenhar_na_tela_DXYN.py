from functools import partial
from typing import Callable, Sequence

from chip8.nucleo import ContextoRuntime, ENDERECO_REGISTRADORES
from chip8.servicos.hexadecimais import (
    hexadecimal_para_binario,
    somar_hexadecimais,
)


def desenhar_na_tela_DXYN(
    instrucao: str,
) -> Callable[[ContextoRuntime], ContextoRuntime]:
    vx = instrucao[1]
    vy = instrucao[2]
    bytes_para_ler = instrucao[3]
    return partial(_desenhar_na_tela, vx, vy, bytes_para_ler)


def _desenhar_na_tela(
    endereco_registrador_x: ENDERECO_REGISTRADORES,
    endereco_registrador_y: ENDERECO_REGISTRADORES,
    bytes_para_ler_da_memoria_a_partir_do_registrador_index: str,
    contexto_runtime: ContextoRuntime,
) -> ContextoRuntime:
    endereco_inicial = contexto_runtime.registradores.i
    assert endereco_inicial is not None
    endereco_final = somar_hexadecimais(
        endereco_inicial, bytes_para_ler_da_memoria_a_partir_do_registrador_index
    )

    sprite = _formar_sprite(contexto_runtime, endereco_inicial, endereco_final)

    contexto_runtime.tela.desenhar_sprite(
        sprite,
        contexto_runtime.registradores[endereco_registrador_x],
        contexto_runtime.registradores[endereco_registrador_y],
    )

    if contexto_runtime.tela.pixel_mudou_1_para_0:
        contexto_runtime.registradores["f"] = "1"
    else:
        contexto_runtime.registradores["f"] = "0"

    return contexto_runtime


def _formar_sprite(
    contexto_runtime: ContextoRuntime, endereco_inicial: str, endereco_final: str
):
    dados_hexadecimais_para_formar_sprite = [
        contexto_runtime.ram[endereco]
        for endereco in range(int(endereco_inicial, 16), int(endereco_final, 16))
    ]

    sprite = _tornar_binario_dados_hexadecimais_para_formar_sprite(
        dados_hexadecimais_para_formar_sprite
    )

    return sprite


def _tornar_binario_dados_hexadecimais_para_formar_sprite(
    dados: Sequence[str],
) -> list[str]:
    dados_binarios = [hexadecimal_para_binario(x) for x in dados]

    validado = []
    for bin_str in dados_binarios:
        b = bin_str
        if bin_str[0:2] == "0b":
            b = bin_str[2:]

        binario_validado = b.zfill(8)
        validado.append(binario_validado)

    return validado
