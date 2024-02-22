from dataclasses import dataclass, field
from typing import Callable

from chip8.nucleo.componentes.ram import Ram
from chip8.nucleo.componentes.registradores import (
    Registradores,
)
from chip8.nucleo.componentes.contador import Contador
from .tela import Tela


def _placeholder(x):
    return x


@dataclass(slots=True)
class ContextoRuntime:
    ultima_execucao: Callable = field(default=_placeholder)
    ultima_instrucao: str = field(default="0000")
    ram: Ram = field(default_factory=Ram)
    registradores: Registradores = field(default_factory=Registradores)
    contador: Contador = field(default_factory=lambda: Contador("200"))
    tela: Tela = field(default_factory=Tela)
