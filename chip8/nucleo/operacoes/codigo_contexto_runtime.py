from typing import Any, Mapping, Union
from chip8.nucleo.dados import e_ram
from chip8.nucleo.dados.tipos import (
    CONTADOR,
    CONTEXTO_RUNTIME,
    CONTEXTO_RUNTIME_FUNC_ATUALIZAR,
    CONTEXTO_RUNTIME_KEYS,
    INSTRUCAO_COMPLETA_CHIP8,
    PIXEL_MAP,
    RAM,
    REGISTRADOR_INDEX,
    REGISTRADORES,
    e_contador,
    e_instrucao,
    e_pixel_map,
    e_registrador,
    e_registrador_index,
)


def ler_contexto_runtime(contexto: CONTEXTO_RUNTIME, chave: CONTEXTO_RUNTIME_KEYS):
    _validar_chave(chave)
    valor = contexto[chave]
    return valor


def escrever_contexto_runtime(
    contexto: CONTEXTO_RUNTIME,
    chave: CONTEXTO_RUNTIME_KEYS,
    valor: Union[
        RAM,
        REGISTRADORES,
        REGISTRADOR_INDEX,
        CONTADOR,
        PIXEL_MAP,
        INSTRUCAO_COMPLETA_CHIP8,
    ],
) -> CONTEXTO_RUNTIME:
    _validar_input(chave, valor)
    return contexto.set(chave, valor)


def escrever_varios_valores_contexto_runtime(
    contexto_runtime: CONTEXTO_RUNTIME,
    relacao_chave_valor: Mapping[CONTEXTO_RUNTIME_KEYS, Any],
) -> CONTEXTO_RUNTIME:
    _validar_varios_inputs(relacao_chave_valor)
    mutar_contexto = contexto_runtime.evolver()

    for chave, valor in relacao_chave_valor.items():
        mutar_contexto[chave] = valor

    novo_contexto = mutar_contexto.persistent()

    return novo_contexto


def atualizar_contexto_runtime(
    contexto_runtime: CONTEXTO_RUNTIME,
    chave: CONTEXTO_RUNTIME_KEYS,
    atualizar_func: CONTEXTO_RUNTIME_FUNC_ATUALIZAR,
) -> CONTEXTO_RUNTIME:
    valor = ler_contexto_runtime(contexto_runtime, chave)
    valor_atualizado = atualizar_func(valor)

    if _validar_input(chave, valor_atualizado):
        return contexto_runtime.set(chave, valor_atualizado)
    else:
        raise Exception(
            f"CONTEXTO RUNTIME: valor '{valor_atualizado}' não é válido para a chave '{chave}'"
        )


def atualizar_varios_valores_contexto_runtime(
    contexto_runtime: CONTEXTO_RUNTIME,
    relacao_chave_atualizar_func: Mapping[
        CONTEXTO_RUNTIME_KEYS, CONTEXTO_RUNTIME_FUNC_ATUALIZAR
    ],
) -> CONTEXTO_RUNTIME:
    chave_valor_atualizado = dict(
        [
            [chave, atualizar_func(ler_contexto_runtime(contexto_runtime, chave))]
            for chave, atualizar_func in relacao_chave_atualizar_func.items()
        ]
    )

    contexto_atualizado = escrever_varios_valores_contexto_runtime(
        contexto_runtime, chave_valor_atualizado
    )  # type: ignore

    return contexto_atualizado


_TYPEGUARDS = {
    "ram": e_ram,
    "registradores": e_registrador,
    "registrador_index": e_registrador_index,
    "contador": e_contador,
    "pixel_map": e_pixel_map,
    "ultima_instrucao": e_instrucao,
    "ultima_execucao": lambda x: True,
}


def _validar_chave(chave: CONTEXTO_RUNTIME_KEYS) -> bool:
    if chave in _TYPEGUARDS.keys():
        return True

    raise Exception(f"CONTEXTO RUNTIME: '{chave}' chave desconhecida")


def _validar_input(chave: CONTEXTO_RUNTIME_KEYS, valor: Any) -> bool:
    _validar_chave(chave)
    validador = _TYPEGUARDS[chave]
    if validador(valor):
        return True

    raise Exception(
        f"CONTEXTO RUNTIME: valor '{valor}' não é válido para a chave '{chave}'"
    )


def _validar_varios_inputs(
    relacao_chave_valor: Mapping[CONTEXTO_RUNTIME_KEYS, Any]
) -> bool:
    for chave, valor in relacao_chave_valor.items():
        _validar_input(chave, valor)

    return True
