from empleado import Empleado
from gerente import Gerente

class Departamento:
    def __init__(self, nombre, gerente):
        self.nombre = nombre
        self.gerente = gerente
        self.empleados = []

    def nombrar_gerente(self, gerente):
        self.gerente = gerente

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)

    def agregar_empleados(self, empleados):
        for dato in empleados:
            nombres, apellidos, cargo, salario = dato
            empleado = Empleado(nombres, apellidos, cargo, salario)
            self.agregar_empleado(empleado)

    def calcular_nomina(self):
        total_nomina = sum(empleado.salario for empleado in self.empleados)
        return total_nomina + self.gerente.calcular_salario()

    def mostrar(self):
        print(f"Departamento: {self.nombre}")
        print(f"Gerente: {self.gerente.nombres} {self.gerente.apellidos}")
        print("Empleados:")
        for empleado in self.empleados:
            print(f"- {empleado.nombres} {empleado.apellidos} ({empleado.cargo})")
