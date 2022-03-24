palabra = input("Dame una palabra ")

def contar_vocales(palabra):
	contador = 0
	for letra in palabra:
		if letra.lower() in "aeiou":
			contador += 1
	return contador

cantidad = contar_vocales(palabra)
print(f"En {palabra} hay: {cantidad} vocales")

