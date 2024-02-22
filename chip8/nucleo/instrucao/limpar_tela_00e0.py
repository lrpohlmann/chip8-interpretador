from chip8.nucleo import ContextoRuntime


def limpar_tela_00e0(contexto_runtime: ContextoRuntime):
    contexto_runtime.tela.limpar_tela()
    return contexto_runtime
