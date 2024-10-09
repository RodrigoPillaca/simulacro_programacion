# crea una funcion que se le pase una lista y sume los elementos positivos

def suma_numeros_positivos(lista: list) -> int | str:
    acumulador_suma = 0
    if lista == []:
        return "lista vacia"
    else: 
        for i in range(len(lista)):
            if lista[i] > 0:
                acumulador_suma += lista[i]
        return acumulador_suma

lista_numeros = [-10, -2, -3, -12, -30]

resultado = suma_numeros_positivos(lista_numeros)
print(resultado)
