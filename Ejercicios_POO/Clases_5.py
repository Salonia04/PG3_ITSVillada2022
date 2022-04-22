class Persona:
    def __init__(self):
        self.nombre = input("Ingrese su nombre: ")
        self.edad = int(input("Ingrese su edad: "))

    def mostrar(self):
        print("Nombre: ", self.nombre)
        print("Edad: ", self.edad)

class Empleado(Persona):
    def __init__(self):
        super().__init__()
        self.sueldo = int(input("Ingrese su sueldo: "))

    def mostrar(self):
        super().mostrar()
        print("Sueldo: ", self.sueldo)
        if self.sueldo > 3000:
            print("Paga impuestos")

Persona1 = Persona()
Persona1.mostrar()

Empleado1 = Empleado()
Empleado1.mostrar()