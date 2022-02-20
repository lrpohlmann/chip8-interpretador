from typing import Any, Callable, Dict, Literal, Mapping, Sequence, Union
from functools import partial


def _formatador_base(a_ser_formatado, formatadores_especificos: Sequence[Callable[[Any], Union[str, None]]]):
    for formatadores_esp in formatadores_especificos:
        resultado = formatadores_esp(a_ser_formatado)
        if resultado:
            return resultado

    return str(a_ser_formatado)


def _dict_str_formatador_mostrar_apenas_valores_nao_nulos(d: Dict) -> str:
    if isinstance(d, Mapping):
        return str(dict([(k, v) for k, v in d.items() if v != None]))


formatador_a = partial(_formatador_base, formatadores_especificos=[
    _dict_str_formatador_mostrar_apenas_valores_nao_nulos])
