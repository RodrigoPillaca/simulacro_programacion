'''Se ingresan un máximo de 10 números o hasta que el usuario ingrese el número 0. Mostrar la suma y el promedio de todos los números.
'''
acumulador = 0
contador = 0

for i in range(10):
    numero = input("ingrese un numero: ")
    numero = int(numero)
    if numero == 0:
        break
     
    acumulador += numero
    contador += 1
    
promedio = acumulador / contador

print(acumulador)
print(promedio)