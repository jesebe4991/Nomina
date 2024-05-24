import unittest
from empresa import Empresa
from departamento import Departamento
from gerente import Gerente
from datos import datos_sistemas, datos_mercadeo, datos_ventas

class TestEmpresa(unittest.TestCase):
    
    def test_creacion_empresa(self):
        departamentos = [
            Departamento('Sistemas', Gerente('Claudia', 'Ruiz', 13 * 1300000)),
            Departamento('Ventas', Gerente('Juan', 'García', 13 * 1300000))
        ]
        empresa = Empresa('Tech Corp', departamentos)
        self.assertEqual(empresa.nombre, 'Tech Corp')
        self.assertEqual(len(empresa.departamentos), 2)
    
    def test_calculo_nomina(self):
        sistemas = Departamento('Sistemas', Gerente('Claudia', 'Ruiz', 13 * 1300000))
        ventas = Departamento('Ventas', Gerente('Juan', 'García', 13 * 1300000))
        sistemas.agregar_empleados(datos_sistemas)
        ventas.agregar_empleados(datos_ventas)
        empresa = Empresa('Tech Corp', [sistemas, ventas])
        self.assertGreater(empresa.calcular_nomina(), 0)

if __name__ == '__main__':
    unittest.main()

