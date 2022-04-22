class Persona:
    def inicializacion(self,nombre,edad):
        self.nombre = input("Ingrese su nombre: ")
        self.edad = int(input("Ingrese su edad: "))

    def mostrar(self):
        print("Nombre: ",self.nombre)
        print("Edad: ",self.edad)