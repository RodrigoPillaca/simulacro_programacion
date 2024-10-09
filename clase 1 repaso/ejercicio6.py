# Escribir un programa que pida al usuario dos números y devuelva su división. Si el usuario introduce el divisor cero debera imprimir un mensaje de error.
numero_dividendo = int(input("ingrese el primer numero: "))
numero_divisor = int(input("ingrese el segundo numero: "))

if numero_divisor == 0:
    print("Error, como divisor debe otro numero que no sea 0")
else:
    resultado_div = numero_dividendo / numero_divisor
    print(resultado_div) 