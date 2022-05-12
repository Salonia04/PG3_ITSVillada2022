meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
while True:
    try:
        mes = int(input("Introduce un numero: "))
        if mes > 0 and mes < 13:
            print(meses[mes-1])
            break
        else:
            print("No existe ese mes amigo ._.")
    except IndexError:
        print("No existe ese mes")