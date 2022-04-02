from chip8.nucleo.operacoes.codigo_call_stack import adicionar_valor_topo_da_stack, obter_valor_topo_da_stack
from testes.fixtures import setup_call_stack


def test_adicionar(setup_call_stack):
    call_stack = setup_call_stack()
    assert len(call_stack) == 0

    nova_call_stack = adicionar_valor_topo_da_stack(call_stack, "104")
    assert len(nova_call_stack) == 1
    assert nova_call_stack[0] == "104"


def test_obter(setup_call_stack):
    call_stack = setup_call_stack(["111", "222"])
    assert len(call_stack) == 2

    nova_call_stack, valor = obter_valor_topo_da_stack(call_stack)
    assert valor == "222"
    assert len(nova_call_stack) == 1
