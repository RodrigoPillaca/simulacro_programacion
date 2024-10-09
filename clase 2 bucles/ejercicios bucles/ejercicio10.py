# JUEGO "Adivinanza del numero"
# Generaremos un número entre 1 y 10.
# Nuestro objetivo es adivinar el número. Si fallamos nos dirán si es mayor o menor que el número buscado. También poner el número de intentos requeridos.

# NOTA IMPORTANTE, estas dos lineas de abajo generan un numero aleatorio entre 1 y 10. 
# Pusimos el print para que vean que cada vez que ejecutan el codigo va a generarse un numero distinto.
# Mas adelante lo vamos a ver, asi que quedense tranquilos. 
# Solamente utilicen la variable numero para realizar el ejercicio.

numero_intentos = int(input("ingrese el numero de intentos: "))
numero = 6

for i in range(numero_intentos):
    numero_ingresado = int(input("ingrese un numero entre el 1 y 10: "))
    while numero_ingresado < 0 or numero_ingresado > 10:
        numero_ingresado = int(input("Error, ingrese un numero entre el 1 y 10: "))
    
    if numero_ingresado == numero:
        print("el numero es correcto")
        break
    elif numero_ingresado < numero:
        print("el numero ingresado es menor")
    else:
        print("el numero ingresado es mayor")

print("se acabaron los intentos")