# Debe crear un programa que permita ingresar una edad (entre 1 y 99 años, validar mediante una funcion) 
# y un género (‘F’, ‘M’,  ‘X’, validar mediante una funcion). En caso de ingresar valores erróneos 
# (edad fuera de rango, o generos inexistentes), informar de esa situación mostrando un mensaje
#  y terminar el programa. Si todos los datos fueron bien ingresados, 
# el programa debe ser capas de indicar, sabiendo que las mujeres se jubilan a los 60 años o mas, 
# los hombres con 65 años o mas, para los no binarios establecemos un promedio de ambas edades.
# Determinar mediante funciones si una persona puede o no jubilarse.

# Declarar variables / constantes....
EDAD_MINIMA = 1
EDAD_MAXIMA = 99
EDAD_JUBILATORIA_MASCULINO = 65
EDAD_JUBILATORIA_FEMENINO = 60

FEMENINO = "F"
MASCULINO = "M"
NO_BINARIO = "X"

# creamos una funcion donde validamos las edades
def validar_edad(edad: int) -> int:
    while edad < EDAD_MINIMA or edad > EDAD_MAXIMA:
        edad = int(input("Error, ingrese una edad valida (entre 1 y 99): "))
    return edad

# creamos una funcion donde validamos el genero
def validar_genero(genero:str) -> str:
    while genero != FEMENINO and genero != MASCULINO and genero != NO_BINARIO:
        genero = (input("Error: Ingrese un genero valido (F, M o X): ")).upper()
    return genero

# Una vez creadas las validaciones comenzamos con la lógica:

# calculo del promedio
PROMEDIO = (EDAD_JUBILATORIA_MASCULINO + EDAD_JUBILATORIA_FEMENINO) / 2

def jubilarse(edad: int, genero: str) -> str:
    mensaje = "Puede jubilarse"
    
    if genero == FEMENINO and edad >= 60:
        return mensaje
    elif genero == MASCULINO and edad >= 65:
        return mensaje
    elif genero == NO_BINARIO and edad >= PROMEDIO:
        return mensaje

# ingresamos los datos 
edad = int(input("Ingrese su edad: "))
edad = validar_edad(edad)
genero = input("Ingrese su genero: ").upper()
genero = validar_genero(genero)

resultado = jubilarse(edad, genero)

print(resultado)

# :D