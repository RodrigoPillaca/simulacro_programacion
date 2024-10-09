# vector = [12, 34, "hola", 65]

# matriz = [
#     [12, 34, 65, 54, 442],
#     [54, 34, 34, 45, 502],
#     [32, 324, 323, 3, 12],
#     [3, 34, 43, 234, 123]
# ]

# print(len(matriz))
# print(range(len(matriz)))

# for i in matriz:
#     for j in i:
#         print(j, end=" ")
#     print("")

# for i in range(len(matriz)):
#     for j in range(len(matriz[i])):
#         print(matriz[i][j], end = " ")
#     print("")


# como crear una matriz
# def inicializar_matriz(filas: int, columnas: int) -> list[list]: # espefica que la listas contiene listas
#     matriz = []
#     for _ in range(filas):
#         fila = [0] * columnas
#         print(fila)
#         matriz += [fila]
#     return matriz

# matriz2x3 = inicializar_matriz(2, 3)
# print(matriz2x3)


# def carga_matriz_secuencialmente(matriz: list[list]) -> list[list]:
#     for i in  range(len(matriz)):
#         for j in range(len(matriz[i])):
#             matriz [i][j]= int(input("Ingrese  tu numero: "))
#     return matriz

# resultado = carga_matriz_secuencialmente(matriz2x3)
# print(resultado)

# for i in  range(len(resultado)):
#     for j in range(len(resultado[i])):
#         print(resultado[i][j], end=" ")
#     print("")
    
    
    
def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return f"fila: {i}, columna: {j}"
    
matriz = [
    [2, 4, 5, 8],
    [6, 3, 9, 18]
]

resultado = buscar_valor(matriz, 9)
print(resultado)