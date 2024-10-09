# Escribir un programa que imprima un patrón como el siguiente teniendo
# como input un 5 (puede ser en Código o diagrama):

# 123454321
# 1234 4321
# 123   321
# 12     21
# 1       1 


numero = 5

for i in range(0, numero):
    for j in range(i):
        print(j+1, i)
    print("")

# lista_numeros= []

# numero = int(input("ingrese el numero"))

# for i in range (numero):
#     lista_numeros.append(i+1)

# for i in range (len(lista_numeros)-1):
#     lista_numeros.append(numero-i-1)

# cadena = ""
# for i in range(len(lista_numeros)):
#     cadena +=str(lista_numeros[i])

# print(cadena)