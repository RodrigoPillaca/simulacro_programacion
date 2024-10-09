# Para pagar un determinado impuesto se debe ser mayor de 18 años y tener unos 
# ingresos iguales o superiores a 20000 ARS mensuales. Escribir un programa que pregunte 
# al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que pagar un impuesto o no.

edad = int(input("ingrese su edad: "))
ingreso_mensual = int(input("ingrese su ingreso mensual: "))

if edad > 17 and ingreso_mensual >= 20000:
    print("usted debe pagar impuestos")
else:
    print("usted no debe pagar impuestos")