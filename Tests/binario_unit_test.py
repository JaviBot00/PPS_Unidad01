import unittest
from src.binario import esBinario

# Debemos crear una clase que hereda de la clase TestCase
class binarioTest(unittest.TestCase):
    
    # setUp se ejecuta siempre antes de ejecutar cada test
    def setUp(self):
        print("Empezando Test...")
    
    # tearDown se ejecuta siempre al finalizar cada test
    def tearDown(self):
        print("Test Ejecutado ...")
    
    # Cada test debe empezar por la palabra test_
    def test_entrynumber(self):
        self.assertTrue(esBinario("10101010110101010101"))
        self.assertFalse(esBinario("869284"))
        self.assertEqual(esBinario("1010"), True)

    def test_negative(self):
        with self.assertRaises(TypeError):
            esBinario(-1)

    def test_isNotInt(self):
        with self.assertRaises(TypeError):
            esBinario("Holaaaa")
            esBinario(False)

# Llamamos a main para que se ejecute el Runner.
if __name__ == '__main__':
    unittest.main()