from src.binario import esBinario

def test_esBinario():
    assert esBinario("101010") == True
    assert esBinario("0") == True
    assert esBinario("1") == True
    assert esBinario("") == True  # Cadena vacía es válida
    assert esBinario("12345") == False  # Números distintos a 0 y 1
    assert esBinario("abcde") == False  # Caracteres no binarios
    assert esBinario("1010a1") == False  # Caracter no binario en medio
    assert esBinario("10101 ") == False  # Espacio al final
    assert esBinario(" 10101") == False  # Espacio al inicio