import math
flag = 0

while(flag == 0):
    ancho = int(input("Dame el ancho del triangulo: "))
    if(ancho%2==0):
        print("NO PUEDE SER PAR >:(")
        flag = 0
    else:
        flag = 1

caracter = input("Dame el caracter que queres usar: ")
espacios = math.floor(ancho/2)

def dibujar_triangulo(ancho, caracter):
    contador = 0
    for i in range(ancho):
        contador = contador + 1
        print(" " * (espacios - i) + caracter * (contador) + " " * (espacios - i))
        contador = contador + 1
        if(i==espacios):
            break

    for i in range(ancho):
        contador = contador - 1
        print(" " * (espacios + i) + caracter * (contador) + " " * (espacios + i))
        contador = contador - 1
        if(i==espacios):
            break
    
        
        
dibujar_triangulo(ancho, caracter)