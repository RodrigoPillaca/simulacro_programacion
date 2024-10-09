# Solicitarle al usuario que ingrese una palabra y que nuestro
# algoritmo cuente cuántas vocales tiene utilizando un bucle for.

palabra = input("ingrese una palabra: ")

contador = 0

for letra in palabra:
    
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        contador += 1

print(f"tiene {contador} vocales")