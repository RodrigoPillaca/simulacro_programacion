# Comenzamos definiendo variables

# Funciones

def validar_nombre(nombre_completo : str) -> bool:
    valido = False
    while not(valido) :
        if nombre_completo == "" or nombre_completo == None:
             valido = False
    return nombre_completo

def validar_edad(edad: int) -> int:
    ''' Funcion que valida que la edad ingresada por el usuario sea mayor a 20 años
    
    Argumentos: edad(int)
    Retornos: edad(int)
    '''
    while edad < 20:        
        edad = int(input("Edad NO VALIDA. Ingrese una edad mayor a 20): "))
    return edad
    
def validar_genero(genero: str) -> str:
    while (genero != "m") and (genero != "f") and (genero != "x"):
          genero = input("Genero no valido, seleccione entre 'f' 'm' 'x': ").lower()
    return genero

#Realizo mostrar actividaes dale
def mostrar_actividades() -> str:
     print()

     
# Variables/Constantes

estudiante_mas_grande = float
total_actividades = 0
genero_m = 'm'
genero_f = 'f'
genero_x = 'x'

ACTIVIDADES = ["Futbol", "Basket", "Voley", "Natacion", "Atletismo"]

contadores = [0, 0, 0, 0, 0]
continuar = "s"

while continuar == "s":
    nombre_completo = input("Ingrese su nombre completo:")
    nombre_completo = validar_nombre(nombre_completo)
    
    edad = int(input("Ingrese su edad: "))
    edad = validar_edad(edad)

    genero = input("Ingrese su genero: ").lower()
    genero = validar_genero(genero)

    activad = input("Ingrese su actividad: ")
    
                
        