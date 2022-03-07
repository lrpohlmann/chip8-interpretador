from functools import partial
from pathlib import Path
from typing import Callable, NewType, Optional
from chip8.nucleo.dados.tipos import RAM
from chip8.servicos.gui import display
from chip8.app.mainloop import mainloop
from chip8.nucleo.operacoes.codigo_ram import carregar_programa_na_ram
from chip8.nucleo.dados.contexto_runtime import criar_contexto_runtime
from chip8.nucleo.operacoes.codigo_contexto_runtime import ler_contexto_runtime, escrever_contexto_runtime
from chip8.nucleo.operacoes.codigo_rom import obter_instrucoes_da_rom

CHIP8_MAINLOOP = Callable


def setup_mainloop(rom: Optional[Path] = None) -> CHIP8_MAINLOOP:
    if not rom:
        rom = _selecionar_rom()
        if not rom:
            exit(code=0)

    instrucoes = obter_instrucoes_da_rom(rom)

    contexto = criar_contexto_runtime()
    ram: RAM = ler_contexto_runtime(contexto, "ram")
    ram_carregada = carregar_programa_na_ram(ram, instrucoes)
    contexto_instrucoes_carregadas = escrever_contexto_runtime(
        contexto, "ram", ram_carregada)

    display.setup_tela()

    return partial(mainloop, contexto_instrucoes_carregadas)


def _selecionar_rom() -> Optional[Path]:
    import tkinter as tk
    import tkinter.filedialog as fd
    root = tk.Tk()
    root.withdraw()
    nome_arquivo = fd.askopenfilename(title="Escolha uma ROM CHIP8", filetypes=(
        ("CHIP8 Rom", "*.ch8"),), initialdir=str(Path.home()), )

    root.destroy()
    if not isinstance(nome_arquivo, str):
        return None

    return Path(nome_arquivo)
