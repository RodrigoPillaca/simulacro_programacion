# Imprime la tabla de multiplicar de un número dado por el usuario, se debe utilizar el bucle while.

numero = input("ingrese un numero: ")
numero = int(numero)
i = 1

while i < 11:
    print(f"{numero} x {i} = {numero * i}")
    i += 1