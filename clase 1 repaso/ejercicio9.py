# Escribí un programa que solicite al usuario una letra y, si es una vocal, muestre el mensaje “Es vocal”. 

letra = input("ingrese una letra: ")

if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
    print("Es vocal")