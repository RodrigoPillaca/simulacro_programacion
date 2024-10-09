# Escribir un programa que almacene la cadena de caracteres prog1Div115 en una variable, 
# pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida 
# por el usuario coincide con la guardada en la variable

contraseña = "prog1Div115"
ingreso_contraseña = input("ingrese una contraseña: ")

if ingreso_contraseña == contraseña:
    print("contraseña correcta")