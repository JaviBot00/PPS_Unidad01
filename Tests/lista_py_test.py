from src.lista import estaEnRango
from src.lista import estaEnLista

def test_estaEnRango():
    assert estaEnRango(5, 1, 10) == True
    assert estaEnRango(1, 1, 10) == True
    assert estaEnRango(10, 1, 10) == True
    assert estaEnRango(15, 1, 10) == False
    assert estaEnRango(0, 1, 10) == False

def test_estaEnLista():
    assert estaEnLista(5, [1, 3, 5, 7, 9]) == True
    assert estaEnLista(1, [1, 3, 5, 7, 9]) == True
    assert estaEnLista(9, [1, 3, 5, 7, 9]) == True
    assert estaEnLista(4, [1, 3, 5, 7, 9]) == False
    assert estaEnLista(10, [1, 3, 5, 7, 9]) == False