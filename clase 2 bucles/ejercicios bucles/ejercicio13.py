# Calcula la suma de todos los números pares del 1 al 50 usando un bucle while.

acumulador_suma = 0
i = 1

while i < 51:
    if i % 2 == 0:
        acumulador_suma += i
    i += 1

print(acumulador_suma)