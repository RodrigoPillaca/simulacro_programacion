# Se tiene una cadena de texto, pero al revés. Al parecer contiene el nombre de un alumno, la nota de un examen y la materia.
# 1. Dar vuelta la cadena y asignarla a una variable llamada cadena_volteada.
# 2. Extraer nombre y apellido, almacenarlo en una variable llamada nombre_alumno
# 3. Extraer la nota y almacenarla en una variable llamada nota.
# 4. Extraer la materia y almacenarla en una variable llamada materia. 
# 5.  Mostrar por pantalla la siguiente estructura, usando la concantenación de cadenas: NOMBRE APELLIDO ha sacado un NOTA en MATERIA

cadena = "acitametaM ,5.8 ,otipeP ordeP"
cadena_invertida = cadena[::-1]

nombre_alumno = cadena_invertida[0:12]
nota_alumno = cadena_invertida[14:17]
materia_alumno = cadena_invertida[19:29]

print(f"{nombre_alumno} ha sacado un {nota_alumno} en {materia_alumno}")
print("{0} ha sacado un {1} en {2}".format(nombre_alumno, nota_alumno, materia_alumno))

