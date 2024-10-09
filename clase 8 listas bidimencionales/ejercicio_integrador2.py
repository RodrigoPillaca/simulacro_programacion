
def validar_nombre_perro(nombre: str) -> str:
    while nombre.isalpha() == False:
        nombre = input("Error, ingrese el nombre del perro: ").lower()
    return nombre

def validar_km(kilometros: str) -> int:
    while kilometros.isdigit() == False:
        kilometros = input("Error, ingrese la cantidad de kilemetros caminados: ")

    kilometros = int(kilometros)
    while kilometros < 1 or kilometros > 50: # por poner un limite maximo de kilometros
        input = validar_km(input("Error, ingrese la cantidad de kilemetros caminados: "))
    return kilometros
    
    
    
flag_max = True
nombre_perro_max = ""
kilometro_max = 0

flag_min = True
nombre_perro_min = ""
kilometro_min = 0

while True:
    nombre_perro = validar_nombre_perro(input("ingrese el nombre del perro: ").lower())
    cant_km = validar_km(input("ingrese la cantidad de kilemetros caminados: "))
    
    
    if cant_km > kilometro_max or flag_max:
        nombre_perro_max = nombre_perro
        kilometro_max = cant_km
        flag_max = False
    
    if cant_km < kilometro_min or flag_min:
        nombre_perro_min = nombre_perro
        kilometro_min = cant_km
        flag_min = False
        
        
        
    pregunta = input("desea seguir ingresando datos (si/no): ").lower()
    while pregunta != "si" and pregunta != "no":
        pregunta = input("Error, desea seguir ingresando datos: ").lower()
    if pregunta == "no":
        break