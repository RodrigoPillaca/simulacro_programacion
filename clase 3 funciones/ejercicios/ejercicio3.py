# Realiza una función llamada area_rectangulo() que devuelva 
# el área del rectángulo a partir de una base y una altura. 
# Calcula el área de un rectángulo de 15 de base y 10 de altura
# Ayuda: El área de un rectángulo se obtiene al multiplicar la base por la altura.

def area_rectangular(base: int, altura: int) -> int:
    resultado = (base* altura) / 2
    return    resultado
    
base = 15
altura = 10

print(area_rectangular(base, altura))