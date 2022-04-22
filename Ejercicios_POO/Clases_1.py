'''Definicion de clases'''
class Persona:
    def inicializar(self,nombre):
        self.nombre = nombre

    def mostrar(self):
        print("Nombre: ",self.nombre)

'''Codigo'''
Persona1 = Persona()
Persona1.inicializar("Artemys")
Persona1.mostrar()

Persona2 = Persona()
Persona2.inicializar("Parzival")
Persona2.mostrar()