from typing import Mapping

from pyrsistent.typing import PMap


def atualizar(m: PMap, atualizacao: Mapping) -> PMap:
    return m.update(atualizacao)
