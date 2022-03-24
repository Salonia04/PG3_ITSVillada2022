anio = int(input("Decime un año: "))
def bisiesto(num):
    if not anio % 4 and (anio % 100 or not anio % 400):
        print("Es bisiesto")
    else:
        print("No es bisiesto")
bisiesto(anio)
            
