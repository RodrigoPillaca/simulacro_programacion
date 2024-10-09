# Solicitarle al usuario que ingrese un número y 
# se muestre su tabla de multiplicar del 1 al 10 utilizando un bucle for.

numero = input("ingrese un numero: ")
numero = int(numero)

for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")