class Alumno:
    def inicializar(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota

    def mostrar(self):
        print("Nombre: ",self.nombre)
        print("Nota: ",self.nota)

    def aprobado(self):
        if self.nota >= 4:
            print("Regular")
        else:
            print("Libre")

Alumno1 = Alumno()
Alumno1.inicializar("Artemys", 5)
Alumno1.mostrar()
Alumno1.aprobado()

Alumno2 = Alumno()
Alumno2.inicializar("Parzival", 3)
Alumno2.mostrar()
Alumno2.aprobado()