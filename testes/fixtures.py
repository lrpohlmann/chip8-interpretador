from pytest import fixture
from typing import List, Optional, Tuple

from chip8.nucleo.componentes.contador import Contador
from chip8.nucleo.componentes.ram import Ram
from chip8.nucleo.componentes.registradores import (
    Registradores,
)
from chip8.nucleo.componentes.contexto_runtime import ContextoRuntime
from chip8.nucleo.componentes.contador import Contador


@fixture
def contexto_runtime():
    return ContextoRuntime()


@fixture
def setup_contexto_runtime():
    def _setup(
        *,
        contador: Optional[Contador] = None,
        ram: Optional[List[Tuple[str, str]]] = None,
        registradores: dict[str, str | None] | None = None
    ):
        ram_ = Ram()
        if ram:
            ram_._ram.update(dict(ram))
        ctx = ContextoRuntime(
            registradores=Registradores(registradores),
            ram=ram_,
            contador=Contador(contador),
        )
        return ctx

    return _setup
