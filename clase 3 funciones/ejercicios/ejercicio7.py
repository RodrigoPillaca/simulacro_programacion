# Escribe una función llamada celsius_a_fahrenheit que tome una temperatura 
# en grados Celsius como argumento y devuelva su equivalente en grados Fahrenheit.

def celsius_a_fahrenheit(grados_celcius):
    
    resultado = (grados_celcius * 1.8) +32
    return f"grados Fahrenheit es: {resultado}"


grados_celcius = int(input("ingrese el grado celcius: "))

resultado = celsius_a_fahrenheit(grados_celcius)
print(resultado)