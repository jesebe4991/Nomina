import unittest
from empleado import Empleado

class TestEmpleado(unittest.TestCase):
    
    def test_creacion_empleado(self):
        empleado = Empleado('Juan', 'Pérez', 'Desarrollador', 5000000)
        self.assertEqual(empleado.nombres, 'Juan')
        self.assertEqual(empleado.apellidos, 'Pérez')
        self.assertEqual(empleado.cargo, 'Desarrollador')
        self.assertEqual(empleado.salario, 5000000)
    
    def test_calculo_salario(self):
        empleado = Empleado('Ana', 'Gómez', 'Tester', 3000000)
        self.assertEqual(empleado.calcular_salario(), 3000000)

if __name__ == '__main__':
    unittest.main()
