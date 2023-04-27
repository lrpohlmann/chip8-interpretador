import pprint
import logging
from typing import Any, Callable, Dict, Iterable, Sequence, TypeVar, ParamSpec
import functools
import inspect

from chip8.servicos.log.formatador import formatador_a

logger = logging.getLogger(name="Funções Execução")
logger.setLevel(logging.NOTSET)

# Aplicando typing no decorador conforme https://rednafi.github.io/reflections/static-typing-python-decorators.html
P = ParamSpec("P")
R = TypeVar("R")


def log_parametros_e_retorno_da_funcao(func: Callable[P, R]):
    @functools.wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        resultado = func(*args, **kwargs)

        logger.debug(
            _log_str_formato(
                func.__name__,
                _formatar_str_log_parametros(
                    _associar_argumentos_com_parametros(func, args, kwargs),
                    formatador_a,  # type: ignore
                ),
                _formatar_str_log_resultado(resultado, formatador_a),
            )
        )
        return resultado

    return wrapper


def _log_str_formato(
    func_name, associacao_argumento_parametro_str: str, resultado_str: str
):
    return f"Função: {func_name}, Parametros: {associacao_argumento_parametro_str}, Resultado: {resultado_str}"


def _formatar_str_log_resultado(
    a_ser_formatado, formatador: Callable[[Any], str]
) -> str:
    str_inicial = "["
    str_final = "]"
    for x in a_ser_formatado:
        str_inicial += formatador(x) + ", "

    return str_inicial + str_final


def _formatar_str_log_parametros(
    a_ser_formatado: Dict, formatador: Callable[[Any], str]
) -> str:
    str_inicial = "{"
    str_final = "}"
    for k, v in a_ser_formatado.items():
        str_inicial += formatador(k) + " : " + formatador(v) + ", "

    associacao_formatada = str_inicial + str_final
    return associacao_formatada


def _associar_argumentos_com_parametros(
    func: Callable, args: Sequence, kwargs: Dict
) -> Dict:
    nome_params_func = inspect.signature(func).parameters.keys()
    parametros_args_e_kwargs_fornecidos = _juntar_parametros(args, kwargs)

    quantidade_parametros_faltantes = len(nome_params_func) - len(
        parametros_args_e_kwargs_fornecidos
    )
    parametros_padrao = list(inspect.signature(func).parameters.values())
    qtd_parametros_padrao = len(parametros_padrao)

    if quantidade_parametros_faltantes == qtd_parametros_padrao:
        return dict(
            zip(nome_params_func, _juntar_parametros(args, kwargs, parametros_padrao))
        )

    elif quantidade_parametros_faltantes < qtd_parametros_padrao:
        differenca_parametros_fornecidos_e_padrao = (
            qtd_parametros_padrao - quantidade_parametros_faltantes
        )

        parametros_padrao_para_completar_parametros_faltantes = parametros_padrao[
            differenca_parametros_fornecidos_e_padrao : len(parametros_padrao) + 1
        ]

        return dict(
            zip(
                nome_params_func,
                _juntar_parametros(
                    args, kwargs, parametros_padrao_para_completar_parametros_faltantes
                ),
            )
        )

    elif quantidade_parametros_faltantes == 0:
        return dict(
            zip(
                nome_params_func,
                _juntar_parametros(parametros_args_e_kwargs_fornecidos),
            )
        )

    else:
        raise Exception()


def _juntar_parametros(
    args: Sequence, kwargs: Dict = {}, padrao: Iterable[inspect.Parameter] = []
) -> Sequence:
    return (
        list(args)
        + list(kwargs.values())
        + [p.default for p in padrao if p.default != inspect.Parameter.empty]
    )
