from chip8.nucleo.operacoes.obter.obter import obter
from testes.fixtures import *


def test_obter_instrucao(contexto_runtime: CONTEXTO_RUNTIME):
    with contexto_runtime.mutate() as c_mutate:
        with c_mutate["ram"].mutate() as r_mutate:
            r_mutate["0"] = "ff"
            r_mutate["1"] = "ff"
            c_mutate["ram"] = r_mutate.finish()

        c_mutate["contador"] = "0"

        contexto_runtime = c_mutate.finish()

    contexto_runtime = obter(
        contexto_runtime)

    assert contexto_runtime["ultima_instrucao"] == "ffff"
    assert contexto_runtime["contador"] == "2"
