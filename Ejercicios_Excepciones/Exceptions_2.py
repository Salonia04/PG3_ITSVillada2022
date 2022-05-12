while True:
    try:
        num1 = int(input("Introduce un numero: "))
        num2 = int(input("Introduce otro numero: "))
        total = num1 / num2
        print(total)
        break
    except ZeroDivisionError:
        print("No se puede dividir entre 0")