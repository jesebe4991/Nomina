from empresa import Empresa
from departamento import Departamento
from gerente import Gerente
from empleado import Empleado

from datos import datos_sistemas, datos_mercadeo, datos_ventas, SMLV

mercadeo = Departamento('Departamento de Mercadeo', Gerente('Julieta', 'Madolnado', 13*SMLV))
mercadeo.agregar_empleados(datos_mercadeo)

ventas = Departamento('Departamento de Ventas', Gerente('Guillermo', 'Palomino Caicedo', 13*SMLV))
ventas.agregar_empleados(datos_ventas)

sistemas = Departamento('Departamento de Sistemas', Gerente('Margarita', 'Lopez Salinas', 13*SMLV))
sistemas.agregar_empleados(datos_sistemas)

empresa = Empresa('Empresa XYZ', [mercadeo, ventas, sistemas])

empresa.mostrar()

