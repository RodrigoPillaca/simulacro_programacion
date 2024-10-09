# Escribir una función a la que se le pase una cadena <nombre> y 
# muestre por pantalla el saludo ¡hola <nombre>!.
# Llamarla dos veces con diferentes cadenas (nombre) en cada llamada


def saludo(nombre: str) -> str:

    return f"¡hola {nombre}!"
    
nombre1 = input("ingrese su nombre: ")
nombre2 = input("ingrese su nombre: ")

print(saludo(nombre1))
print(saludo(nombre2))