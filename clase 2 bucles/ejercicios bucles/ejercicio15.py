# Validación de entrada:
# Solicita al usuario un número entre 1 y 10, 
# y sigue solicitando hasta que se ingrese un valor válido.

while True:
    numero = int(input("ingrese un numero entre 1 y 10: "))
    while numero < 1 or numero > 10:
        numero = int(input("Error, ingrese un numero entre 1 y 10: "))
    
    if numero > 0 and numero < 11:
        print("perfecto!!!")
        break