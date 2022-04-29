class Familia:
    def __str__(self):
        self.madre = input("Ingrese el nombre de la madre: ")
        self.padre = input("Ingrese el nombre del padre: ")
        self.hijos = []
        self.hijos.append(input("Ingrese el nombre del hijo: "))
        if (self.hijos == "0"):
            pass
    def mostrar(self):
        print("Madre: ", self.madre)
        print("Padre: ", self.padre)
        print("Hijos: ", self.hijos)

Familia1 = Familia()
Familia1.mostrar()
        
