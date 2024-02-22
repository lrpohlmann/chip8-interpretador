from chip8.nucleo.componentes import ContextoRuntime
from chip8.nucleo.instrucao import (
    desenhar_na_tela_DXYN,
    escrever_no_registrador_index_ANNN,
    escrever_no_registrador_vx_6XNN,
    jump_1NNN,
    limpar_tela_00e0,
    somar_no_registrador_vx_7XNN,
)
from chip8.servicos.inteiros.conversao import inteiros_para_hexadecimais


TAMANHO_PROGRAMA = int


class Chip8:
    ENDERECO_INICIO_INSTRUCOES = 512  # hexadecimal: 200
    ENDERECO_MAXIMO_RAM = 4095

    def __init__(self, ctx: ContextoRuntime | None = None):
        if ctx is None:
            self.contexto = ContextoRuntime()
            return

        self.contexto = ctx

    def carregar_programa(self, caminho: str) -> TAMANHO_PROGRAMA:
        with open(str(caminho), "rb") as rom:
            bytes_string = rom.readlines()[0]

        hex_list = bytes_string.hex(":", 1).split(":")

        par_endereco_e_meia_instrucao = tuple(
            zip(
                range(self.ENDERECO_INICIO_INSTRUCOES, self.ENDERECO_MAXIMO_RAM + 1),
                hex_list,
            )
        )

        for endereco, meia_instrucao in par_endereco_e_meia_instrucao:
            self.contexto.ram[inteiros_para_hexadecimais(endereco)] = meia_instrucao

        return len(par_endereco_e_meia_instrucao)

    def obter(self):
        parte_instrucao = []
        parte_instrucao.append(self.contexto.ram[self.contexto.contador.atual()])
        self.contexto.contador.incrementar()
        parte_instrucao.append(self.contexto.ram[self.contexto.contador.atual()])
        self.contexto.contador.incrementar()

        instrucao_completa = f"{parte_instrucao[0]}{parte_instrucao[1]}"
        self.contexto.ultima_instrucao = instrucao_completa

    def decodificar(self):
        instrucao = self.contexto.ultima_instrucao
        if instrucao == "00e0":
            self.contexto.ultima_execucao = limpar_tela_00e0

        elif instrucao[0] == "1":
            self.contexto.ultima_execucao = jump_1NNN(instrucao)

        elif instrucao[0] == "6":
            self.contexto.ultima_execucao = escrever_no_registrador_vx_6XNN(instrucao)

        elif instrucao[0] == "7":
            self.contexto.ultima_execucao = somar_no_registrador_vx_7XNN(instrucao)

        elif instrucao[0] == "a":
            self.contexto.ultima_execucao = escrever_no_registrador_index_ANNN(
                instrucao
            )

        elif instrucao[0] == "d":
            self.contexto.ultima_execucao = desenhar_na_tela_DXYN(instrucao)

        else:
            raise Exception(f"DECODIFICAÇÃO: instrução {instrucao} desconhecida.")

    def executar(self):
        self.contexto.ultima_execucao(self.contexto)

    def mainloop(self):
        while True:
            self.obter()
            self.decodificar()
            self.executar()
