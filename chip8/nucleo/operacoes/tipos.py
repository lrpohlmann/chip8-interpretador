from typing import (Callable)

from chip8.nucleo.dados.tipos import (CONTEXTO_RUNTIME)

FUNCOES_EXECUCAO = Callable[[CONTEXTO_RUNTIME], CONTEXTO_RUNTIME]
