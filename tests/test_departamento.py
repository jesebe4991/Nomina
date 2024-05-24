import unittest
from departamento import Departamento
from gerente import Gerente
from datos import datos_sistemas

class TestDepartamento(unittest.TestCase):
    
    def test_creacion_departamento(self):
        gerente = Gerente('Claudia', 'Ruiz', 13 * 1300000)
        departamento = Departamento('TI', gerente)
        self.assertEqual(departamento.nombre, 'TI')
        self.assertEqual(departamento.gerente, gerente)
        self.assertEqual(len(departamento.empleados), 0)
    
    def test_agregar_empleados(self):
        gerente = Gerente('Claudia', 'Ruiz', 13 * 1300000)
        departamento = Departamento('TI', gerente)
        departamento.agregar_empleados(datos_sistemas)
        self.assertEqual(len(departamento.empleados), len(datos_sistemas))
    
    def test_calculo_nomina(self):
        gerente = Gerente('Claudia', 'Ruiz', 13 * 1300000)
        departamento = Departamento('TI', gerente)
        departamento.agregar_empleados(datos_sistemas)
        self.assertGreater(departamento.calcular_nomina(), 0)

if __name__ == '__main__':
    unittest.main()
