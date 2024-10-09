# Cree un programa que calcule el IMC (Indice de masa corporal). Formula --> IMC=Peso/Altura2 (Peso sobre altura al cuadrado)
# El usuario debera ingresar su peso y su altura (su nombre si quieren y despues imprimirlo concatenado) y el programa ademas de 
# calcular el IMC debera decir en que clasificacion se encuentra.
# La clasificacion la encontraran el archivo de imagen: IMC_clasificacion.jpg

peso = float(input("ingrese su peso: "))
altura = float(input("ingrese su altura: "))

imc = int(peso / altura**2)

if imc < 18.5:
    print("Bajo peso")
elif imc < 24.9:
    print("Adecuado")
elif imc < 29.9:
    print("Sobrepeso")
elif imc < 34.9:
    print("Obecidad grado 1")
elif imc < 39.9:
    print("Obecidad grado 2")
else:
    print("Obecidad grado 2")