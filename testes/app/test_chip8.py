from chip8.app import Chip8


def test_carregar_programa():
    c8 = Chip8()
    tamanho_programa = c8.carregar_programa("rom/IBM Logo.ch8")
    for n in range(512, 512 + tamanho_programa):
        assert c8.contexto.ram[n] is not None


def test_obter():
    c8 = Chip8()
    c8.contexto.ram[512] = "00"
    c8.contexto.ram[513] = "00"
    c8.obter()
    assert c8.contexto.ultima_instrucao == "0000"
    assert c8.contexto.contador == "202"
