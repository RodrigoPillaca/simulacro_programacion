# Escribir un programa para una empresa que tiene salas de juegos para todas las edades y 
# quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. 
# El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. 
# Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 80 ARS y si es mayor de 18 años, 150 ARS.

edad = int(input("ingrese su edad: "))

if edad < 4:
    print("pase gratis")
elif edad < 18:
    print("para entrar debe pagar 80ARS")
else:
    print("para entrar debe pagar 150ARS")
    