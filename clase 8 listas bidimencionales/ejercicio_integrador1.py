
def validar_nombre(nombre: str) -> str:
    while nombre.isalpha() == False:
        nombre = input("Error, ingrese su nombre: ")        
    return nombre

def validar_edad(edad: str) -> int:
    while edad.isdigit() == False:
        edad = input("Error, ingrese su edad: ")
    
    edad = int(edad)
    while edad < 1 or edad > 100:
        # edad = int(input("Error, ingrese su edad: "))
        edad = validar_edad(input("Error, ingrese su edad: "))
    return edad

def validar_sintoma(sintoma: str) -> str:
    while sintoma != "fiebre" and sintoma != "dolor de cabeza" and sintoma != "otro":
        sintoma = input("Error, ingrese su sintoma (fiebre, dolor de cabeza, otro): ").lower()
    return sintoma

def recomendaciones_sintoma(sintoma: str) -> str:
    texto = ""
    if sintoma == "fiebre":
        texto = "Consultar sobre posibles infecciones."
    elif sintoma == "dolor de cabeza":
        texto = "Posible estrés o migraña." 
    else:
        texto = "Síntoma no identificado, consultar más detalles"
    return texto

contador_pacientes_fiebre = 0
contador_pacientes_dolor_cabeza = 0

acumulador_suma_edad = 0
contador_edad = 0

flag_edad = True
edad_joven = 0
nombre_joven = ""
sintoma_joven = ""

while True:
    nombre_paciente = validar_nombre(input("Ingrese el nombre del paciente: "))
    edad_paciente = validar_edad(input("Ingrese su edad: "))
    sintoma = input("Ingrese su sintoma (fiebre, dolor de cabeza, otro): ").lower()
    respuesta_val_sintoma = validar_sintoma(sintoma)
    respuesta_reco_sintoma = recomendaciones_sintoma(sintoma)
    print(f"se le recomienda {respuesta_reco_sintoma}")
    print("------------------------------------------")
    
    if sintoma == "fiebre":
        contador_pacientes_fiebre += 1
    elif sintoma == "dolor de cabeza":
        contador_pacientes_dolor_cabeza += 1
    
    acumulador_suma_edad += edad_paciente
    contador_edad += 1
    
    if edad_joven > edad_paciente or flag_edad:
        edad_joven = edad_paciente
        nombre_joven = nombre_paciente
        sintoma_joven = respuesta_val_sintoma
        flag_edad = False
        
    pregunta = input("desea seguir ingresando datos (si/no): ").lower()
    while pregunta != "si" and pregunta != "no":
        pregunta = input("Error, desea seguir ingresando datos: ").lower()
    if pregunta == "no":
        break
    
promedio = acumulador_suma_edad / contador_edad

print(f"el promedio de edad de los pacientes es de: {promedio}")
print(f"la cantidad de pacientes que consultaron por fiebre es de {contador_pacientes_fiebre} y de dolor de cabeza es de {contador_pacientes_dolor_cabeza}")
print(f"los datos del paciente mas joven es: nombre: {nombre_joven}, edad: {edad_joven}, sintoma: {sintoma_joven}")


