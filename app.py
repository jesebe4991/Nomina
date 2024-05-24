from empresa import Empresa
from departamento import Departamento
from gerente import Gerente
from datos import datos_sistemas, datos_mercadeo, datos_ventas

def main():
    mercadeo = Departamento('Departamento de Mercadeo', Gerente('Julieta', 'Madolnado', 13*1300000))
    mercadeo.agregar_empleados(datos_mercadeo)

    ventas = Departamento('Departamento de Ventas', Gerente('Guillermo', 'Palomino Caicedo', 13*1300000))
    ventas.agregar_empleados(datos_ventas)

    sistemas = Departamento('Departamento de Sistemas', Gerente('Margarita', 'Lopez Salinas', 13*1300000))
    sistemas.agregar_empleados(datos_sistemas)

    empresa = Empresa('Empresa XYZ', [mercadeo, ventas, sistemas])

    empresa.mostrar()

if __name__ == "__main__":
    main()