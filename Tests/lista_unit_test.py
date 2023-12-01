import unittest
from src.lista import estaEnRango
from src.lista import estaEnLista

# Debemos crear una clase que hereda de la clase TestCase
class listaTest(unittest.TestCase):
    
    # setUp se ejecuta siempre antes de ejecutar cada test
    def setUp(self):
        print("Empezando Test...")
    
    # tearDown se ejecuta siempre al finalizar cada test
    def tearDown(self):
        print("Test Ejecutado ...")
    
    # Cada test debe empezar por la palabra test_
    def test_estaEnRango(self):
        self.assertTrue(estaEnRango(5, 1, 10))
        self.assertTrue(estaEnRango(1, 1, 10))
        self.assertTrue(estaEnRango(10, 1, 10))
        self.assertFalse(estaEnRango(15, 1, 10))
        self.assertFalse(estaEnRango(0, 1, 10))

    def test_estaEnLista(self):
        self.assertTrue(estaEnLista(5, [1, 3, 5, 7, 9]))
        self.assertTrue(estaEnLista(1, [1, 3, 5, 7, 9]))
        self.assertTrue(estaEnLista(9, [1, 3, 5, 7, 9]))
        self.assertFalse(estaEnLista(4, [1, 3, 5, 7, 9]))
        self.assertFalse(estaEnLista(10, [1, 3, 5, 7, 9]))

# Llamamos a main para que se ejecute el Runner.
if __name__ == '__main__':
    unittest.main()