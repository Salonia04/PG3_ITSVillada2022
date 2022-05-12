while True:
    try:
        num1 = int(input("Introduce un numero: "))
        num2 = int(input("Introduce otro numero: "))
        total = num1 + num2
        print(total)
        break
    except ValueError:
        print("Tiene que ser un numero >:/")

print("Queres seguri sumando valores?")
sn = input("(si/no): ")
if sn == "si":
    while True:
        try:
            num3 = int(input("Introduce un numero: "))
            total = total + num3
            print(total)
        except ValueError:
            print("Tiene que ser un numero >:/")
else:
    print("Nos re vimos :P")

