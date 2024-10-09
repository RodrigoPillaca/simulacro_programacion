# Dadas las siguientes listas:
# edades = [25,36,18,23,45]
# nombre = ["Juan","Ana","Sol","Mario","Sonia"]
# y considerando que la posición en la lista corresponde a la misma persona,
# mostar el nombre de la persona más joven

EDADES = [25,36,18,23,45]
NOMBRE = ["Juan","Ana","Sol","Mario","Sonia"]

def persona_mas_joven(EDADES: list, NOMBRE: list) -> str :
    edad_minima = float("inf")
    
    for i in range(len(EDADES)):
        if EDADES[i] < edad_minima:
            edad_minima = EDADES[i]
            nombre_joven = NOMBRE[i]
    return f"la persona mas joven es {nombre_joven} con {edad_minima} años"
        
resultado = persona_mas_joven(EDADES, NOMBRE)
print(resultado)

# otras forma de resolver
edades = [25,36,18,23,45]
nombres = ["Juan","Ana","Sol","Mario","Sonia"]
edad_minima = 0
bandera_edad = False

for i in range(len(edades)):
  edad = edades[i]
  nombre = nombres[i]

  if bandera_edad == False or edad < edad_minima:
    edad_minima = edad
    bandera_edad = True


print(f"La persona mas joven es {nombre} con {edad_minima} años de edad")


