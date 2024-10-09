# Escribí un programa que solicite al usuario el ingreso de dos números diferentes y muestre en pantalla al mayor de los dos.
# Y si son iguales tambien mostrar por pantalla que son iguales.

numero1 = int(input("ingrese el primer numero: "))
numero2 = int(input("ingrese el segundo numero: "))

if numero1 > numero2:
    print(f"numero mayor es: {numero1}")
elif numero2 > numero1:
    print(f"numero mayor es: {numero2}")
else:
    print(f"numeros iguales: {numero1} y {numero2}")