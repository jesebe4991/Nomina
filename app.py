from empresa import Empresa
from departamento import Departamento
from gerente import Gerente
from datos import datos_sistemas, datos_mercadeo, datos_ventas

def main():
    mercadeo = Departamento('Departamento de Mercadeo', Gerente('Juana', 'Piedraita', 13*1300000))
    mercadeo.agregar_empleados(datos_mercadeo)

    ventas = Departamento('Departamento de Ventas', Gerente('Carlos', 'Villgran Morales', 13*1300000))
    ventas.agregar_empleados(datos_ventas)

    sistemas = Departamento('Departamento de Sistemas', Gerente('Fulanito', 'Perenseo Morenseo', 13*1300000))
    sistemas.agregar_empleados(datos_sistemas)

    empresa = Empresa('Empresa El Gato que esta triete y azul', [mercadeo, ventas, sistemas])

    empresa.mostrar()

if __name__ == "__main__":
    main()