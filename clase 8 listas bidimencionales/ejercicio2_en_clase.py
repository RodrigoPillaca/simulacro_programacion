# Desarrollar una función que reciba por parámetro, una lista de números
# y un número especificado. La misma debe buscar el número especificado en la lista
# y retornar "True" si existe. Si no existe retornar "False"

# def busqueda_de_numeros(lista_numeros: list, numero: int) -> bool:
#     for i in range(len(lista_numeros)):
#         if lista_numeros[i] == numero:
#             return True
#     return False

# lista_numeros = [1, 2, 3, 4]
# numero = 3

# resultado = busqueda_de_numeros(lista_numeros, numero)
# print(resultado)

def busqueda_de_numeros(lista_numeros: list, numero: int) -> bool:
    for i in range(len(lista_numeros)):
        for j in range(i+1, len(lista_numeros)):
            if lista_numeros[i] + lista_numeros[j] == numero:
                return True
    return False

lista_numeros = [1, 2, 3, 4]
numero = 7

resultado = busqueda_de_numeros(lista_numeros, numero)
print(resultado)