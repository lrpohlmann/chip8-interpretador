from chip8.nucleo.dados.tipos import CONTADOR, e_contador


def criar_contador(inicio: str = "200") -> CONTADOR:
    if e_contador(inicio):
        return inicio
    else:
        raise Exception()
