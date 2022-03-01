from typing import Optional, Tuple
from chip8.nucleo.dados.contador import criar_contador


def test_falhar_criar_contador():
    def falhou(func, *args, **kwargs) -> Tuple[bool, Optional[Exception]]:
        try:
            func(*args, **kwargs)
            return (False, None)
        except Exception as e:
            return (True, e)

    casos = ["zzzz", 1]
    for caso in casos:
        assert falhou(criar_contador, caso)[0]


def test_criar_contador():
    criar_contador()
    criar_contador("a")
    criar_contador("fff")
