from chip8.nucleo.dados.tipos import CONTADOR
from chip8.servicos.hexadecimais.aritimetica import somar_hexadecimais


def _incrementar_contador(contador: CONTADOR, incr: str) -> CONTADOR:
    return somar_hexadecimais(contador, incr)


def incrementar_contador_por_um(contador: CONTADOR) -> CONTADOR:
    return _incrementar_contador(contador, "1")


def incrementar_contador_por_dois(contador: CONTADOR) -> CONTADOR:
    return _incrementar_contador(contador, "2")
