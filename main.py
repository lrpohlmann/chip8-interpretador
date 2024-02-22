from chip8.app import Chip8

c8 = Chip8()
c8.carregar_programa("rom/IBM Logo.ch8")
c8.mainloop()
