import unittest
from gerente import Gerente

class TestGerente(unittest.TestCase):
    
    def test_creacion_gerente(self):
        gerente = Gerente('Carlos', 'Rodríguez', 13 * 1300000)
        self.assertEqual(gerente.nombres, 'Carlos')
        self.assertEqual(gerente.apellidos, 'Rodríguez')
        self.assertEqual(gerente.cargo, 'Gerente')
        self.assertEqual(gerente.salario, 16900000)
    
    def test_calculo_salario(self):
        gerente = Gerente('Laura', 'Martínez', 13 * 1300000)
        self.assertEqual(gerente.calcular_salario(), 16900000)

if __name__ == '__main__':
    unittest.main()
