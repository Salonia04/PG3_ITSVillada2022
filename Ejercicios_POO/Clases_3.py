class Triangulo:
    def inicializar(self,lado1,lado2,lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
        if self.lado1 > self.lado2 and self.lado1 > self.lado3:
            self.ladoMayor = self.lado1
        elif self.lado2 > self.lado1 and self.lado2 > self.lado3:
            self.ladoMayor = self.lado2
        else:
            self.ladoMayor = self.lado3

    def mostrar(self):
        print("Lado 1: ", self.lado1)
        print("Lado 2: ", self.lado2)
        print("Lado 3: ", self.lado3)
        print("Lado mayor: ", self.ladoMayor)
    
    def forma(self):
        if self.lado1 == self.lado2 and self.lado2 == self.lado3:
            print("Equilatero :)")
        else:
            print("No es equilatero :(")

Triangulo = Triangulo()
Triangulo.inicializar(4, 2, 6)
Triangulo.mostrar()
Triangulo.forma()