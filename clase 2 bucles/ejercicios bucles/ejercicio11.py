# Solicitar al usuario ingresar los tres lados de un triángulo e indicar de qué tipo es:
# Isósceles: 2 lados iguales
# Equilátero: 3 lados iguales
# Escaleno: 0 lados iguales


lado1 = int(input("ingrese el primer lado (por ej: 7): "))
lado2 = int(input("ingrese el segundo lado (por ej: 7): "))
lado3 = int(input("ingrese el tercer lado (por ej: 7): "))

if  lado1 == lado2 and lado1 == lado3:
    print("es un triangulo Equilátero")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("es un triangulo Isóceles")
else:
    print("es un triangulo Escaleno")