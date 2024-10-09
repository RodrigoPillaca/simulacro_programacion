# Desarrollar una función que invierte el orden de los caracteres en una cadena. Utilizar Slicing
# slicing

def invertir_palabra(cadena: str) -> str:
    return cadena[::-1]

cadena = "python"
respuesta = invertir_palabra(cadena) 

print(respuesta)