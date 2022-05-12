#Almacenar una serie de string en un archivo de texto. Tratar de llamar al método 'write' pasando un entero. Capturar la excepcion correspondiente.
while True:
    try:
        with open("archivo.txt", "w") as archivo:
            archivo.write("Hola ")
            archivo.write("Mundo")
            archivo.write("!")
            break
    except TypeError:
        print("Tiene que ser un string .-.")