from chip8.servicos.hexadecimais.conversao import hexadecimal_para_inteiro


def numero_ira_setar_o_vf(numero: str) -> bool:
    if hexadecimal_para_inteiro(numero) > 255:
        return True
    else:
        return False
