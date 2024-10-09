numero1 = int(input("ingrese el primer numero: "))
numero2 = int(input("ingrese el primer numero: "))

def sumar(num1: int, num2: int) -> int:
    resultado = num1 + num2
    return resultado 
sumar(numero1, numero2)

def restar(num1: int, num2: int) -> int:
    resultado = num1 - num2
    return resultado 
restar(numero1, numero2)

def multiplicar(num1: int, num2: int) -> int:
    resultado = num1 * num2
    return resultado 
multiplicar(numero1, numero2)

def division(num1: int, num2: int) -> int:
    if num2 != 0:
        resultado = num1 / num2
        return resultado 
    else:
        return 0
division(numero1, numero2)