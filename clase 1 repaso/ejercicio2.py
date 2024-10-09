# Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.

numero = input("ingrese un numero: ")
numero = int(numero)

if numero % 2 == 0:
    print("El numero ingresado es par")
else:
    print("El numero ingresado es impar")

