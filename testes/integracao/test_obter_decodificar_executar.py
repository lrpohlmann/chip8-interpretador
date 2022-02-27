from testes.fixtures import contexto_runtime
from chip8.nucleo.operacoes.codigo_ram import ler_memoria_ram, escrever_na_memoria_ram, obter_instrucao_completa_da_memoria_e_incrementar_contador
from chip8.app.decodificar import decodificar
from chip8.nucleo.dados.tipos import CONTEXTO_RUNTIME


def test_obter_decodificar_executar_6XNN(contexto_runtime: CONTEXTO_RUNTIME):
    escrever_na_memoria_ram(contexto_runtime["ram"], "200", "60")
    escrever_na_memoria_ram(contexto_runtime["ram"], "201", "ff")

    instrucao_completa, novo_contador = obter_instrucao_completa_da_memoria_e_incrementar_contador(
        contexto_runtime["ram"], "200")

    contexto_runtime_com_contador_atualizado = contexto_runtime.set(
        "contador", novo_contador)

    func_exec = decodificar(instrucao_completa)

    contexto_runtime_atualizado = func_exec(
        contexto_runtime_com_contador_atualizado)

    assert contexto_runtime_atualizado["registradores"]["0"] == "ff"
    assert contexto_runtime_atualizado["registrador_index"] == {"i": None}
    assert contexto_runtime_atualizado["contador"] == "202"
