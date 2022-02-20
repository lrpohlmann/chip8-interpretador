from functools import reduce
from operator import sub


def somar_hexadecimais(*args: str):
    return hex(
        sum(
            map(
                lambda x: int(x, 16), args
            )
        )
    ).replace("0x", "", 1)


def subtrair_hexadecimais(*args: str):
    return hex(
        reduce(
            lambda x, y: sub(x, y),
            map(
                lambda x: int(x, 16),
                args
            )
        )
    ).replace("0x", "", 1)
