from chip8.nucleo import Contador


def test_incrementar():
    c = Contador("200")
    c.incrementar()
    c.atual() == "201"
