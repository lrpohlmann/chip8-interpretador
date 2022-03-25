from chip8.servicos.hexadecimais.conversao import hexadecimal_para_inteiro


def numero_ira_setar_o_vf(numero: str) -> bool:
    num_int = hexadecimal_para_inteiro(numero)
    if num_int > 255 or num_int < 0:
        return True
    else:
        return False
