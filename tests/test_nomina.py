import unittest
from datos import SMLV
from empleado import Empleado
from gerente import Gerente
from departamento import Departamento
from empresa import Empresa

class TestNomina(unittest.TestCase):
    def setUp(self):
        self.gerente = Gerente("Gerente", "Prueba", 13 * SMLV)
        self.empleado1 = Empleado("Empleado1", "Prueba", "Cargo1", 3000000)
        self.empleado2 = Empleado("Empleado2", "Prueba", "Cargo2", 4000000)
        self.departamento = Departamento("Departamento de Prueba", self.gerente)
        self.departamento.agregar_empleado(self.empleado1)
        self.departamento.agregar_empleado(self.empleado2)
        self.empresa = Empresa("Empresa de Prueba", [self.departamento])

    def test_calcular_salario_gerente(self):
        self.assertEqual(self.gerente.calcular_salario(), 13 * SMLV)

    def test_calcular_nomina_departamento(self):
        self.assertEqual(self.departamento.calcular_nomina(), 3000000 + 4000000 + 13 * SMLV)

    def test_calcular_nomina_empresa(self):
        self.assertEqual(self.empresa.calcular_nomina(), 3000000 + 4000000 + 13 * SMLV)

    def test_mostrar_empresa(self):
        self.empresa.mostrar()  

if __name__ == "__main__":
    unittest.main()
