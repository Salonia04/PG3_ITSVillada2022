lista = [4,7,10,19,20,77,99,]
print(lista)
buscar = int(input("Decime un numero para buscar: "))

def funcion(lista, buscar):
    if buscar in lista:
        print(lista.index(buscar))
    else:
        print("Este numero no esta en la lista :'(")

funcion(lista, buscar)