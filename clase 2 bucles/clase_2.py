# rango = range(5)
# print(rango)
# print(list(rango))

# -------------------------
# rango = range(0, 5)
# print(rango)
# print(list(rango))

# ------------------------
# rango = range(3, 9)
# print(rango)
# print(list(rango))

# ------------------------
# rango = range(0, 9, 3)
# print(rango)
# print(list(rango))

# ------------------------
# rango = range(10, 0, -2)
# print(rango)
# print(list(rango))

# -----------------------
# for

# con variable de control i
# for i in range(5):
#     print(i)
    
# sin variable de control _
# for _ in range(5):
#     print("hola")

# ----------------------- 
# acumulador = 0
# contador_pares = 0

# for i in range(5):
#     numero = input("ingrese un numero: ")
#     numero = int(numero)
#     while numero == 0:
#         numero = input("ingrese un numero que no sea 0: ")
#         numero = int(numero)
#     if numero % 2 == 0:
#         contador_pares += 1
    
#     acumulador += numero
    
# print(acumulador)
# print(contador_pares)

# -------------------------------
# break rompe la estructura repetitiva

# acumulador = 0
# contador_pares = 0

# for i in range(5):
#     while True:
#         numero = input("ingrese un numero que no sea 0: ")
#         numero = int(numero)
#         if numero != 0:
#             break
#         else:
#             print("Error, reingrese")
            
#     if numero % 2 == 0:
#         contador_pares += 1
    
#     acumulador += numero
    
# print(acumulador)
# print(contador_pares)

# ---------------------------
# for i in range(10):
#     if i == 4:
#         break
#     print(i)

# print ("fin")

# ---------------------------
# for i in  range(5):
#     numero = input("ingrese un numero: ")
#     numero = int(numero)
#     if numero % 5 == 0:
#         break
    
#     print(numero)
    
# --------------------------
# continue saltea dicha parte, pero no rompe el bucle

# for i in  range(5):
#     numero = input("ingrese un numero: ")
#     numero = int(numero)
#     if numero % 2 != 0:
#         continue 
#     print(numero)
    
# ---------------------------
for i in  range(5):
    print(f"{i}: rojo")
    for j in range(3):
        print(f"{j}: verde")
    