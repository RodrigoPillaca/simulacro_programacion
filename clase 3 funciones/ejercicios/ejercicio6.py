# Escribe una función llamada calculadora que tome tres argumentos:
# dos números y un operador (+, -, *, /). La función debe realizar 
# la operación correspondiente y devolver el resultado.
# Deben tener en cuenta el error de la division por 0 y que no ocurra.

# Extra: se puede realizar un breve menu en donde el usuario puede
# seleccionar:
#  1. Utilizar calculador
#  2. Salir
# si el usuario no ingresa 1 o 2, mostrarle un mensaje que no es una
# opcion correcta.


def calculadora(numero1, numero2, operador):
        if operador == "+":
            return numero1 + numero2
        elif operador == "-":
            return numero1 - numero2
        elif operador == "*":
            return numero1 * numero2
        else:
            if numero1 == 0 or numero2 == 0:
                return "no se puede devidir por 0 (cero)"
            else:
                return numero1 / numero2

pregunta = int(input("""
                 seleccione (1 o 2)
                    1. Utilizar calculador
                    2. Salir
                 : """))

if pregunta == 1:
    numero1 = int(input("ingrese el primer número: "))
    numero2 = int(input("ingrese el segundo número: "))
    operador = input("ingrese el operador (+, -, *, /): ")

    print(calculadora(numero1, numero2, operador))
else:
    print("perfecto")


