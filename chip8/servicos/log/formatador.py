from typing import Any, Callable, Dict, Literal, Sequence, Union
from collections.abc import Mapping
from functools import partial, singledispatch

from immutables import Map


def _formatador_base(a_ser_formatado, formatador_especifico: Callable[[Any], str]):
    return formatador_especifico(a_ser_formatado)


@singledispatch
def _formatador_especifico(obj: object):
    return str(obj)


@_formatador_especifico.register
def _str(obj: str):
    return obj


@_formatador_especifico.register
def _dict_str_formatador_mostrar_apenas_valores_nao_nulos(obj: Mapping):
    em_sequencia = sorted(list(obj.items()), key=lambda x: x[0])
    dicio_para_transformar_em_str: Dict[str, str] = {}
    for k, v in em_sequencia:
        if v == None:
            continue

        sub_formatador = _formatador_especifico.dispatch(type(v))

        dicio_para_transformar_em_str[k] = sub_formatador(v)

    return str(dicio_para_transformar_em_str)


formatador_a = partial(
    _formatador_base, formatador_especifico=_formatador_especifico)
