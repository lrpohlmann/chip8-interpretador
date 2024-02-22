from collections import UserString

from chip8.servicos.hexadecimais.aritimetica import somar_hexadecimais


class Contador(UserString):
    def incrementar(self):
        self.data = somar_hexadecimais(self.data, "1")

    def atualizar(self, novo_endereco: str):
        self.data = novo_endereco

    def atual(self):
        return self.data
