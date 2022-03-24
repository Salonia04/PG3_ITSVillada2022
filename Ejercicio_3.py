ancho = int(input("Dame el ancho: "))
alto = int(input("Dame el alto: "))
caracter = input("Dame el caracter: ")

def tabla():
    for i in range(alto):
        for j in range(ancho):
            print(caracter, end="")
        print()
tabla()
