# Realizar una función llamada par_o_impar:

# 1-Recibirá un número por parámetro
# 2-Imprimirá Par si el número es par
# 3-Imprimirá Impar si el número es impar
# 4-Si se ingresa algo que no sea número debe indicar 
# que se ingrese un número. (Para pensar un poco más)

def par_o_impar(numero) -> int:
    if numero % 2 == 0:
        return "par"
    else:
        return "impar"

numero = input("ingrese un número: ")
while numero.isnumeric() == False:
    numero = input("Error, ingrese un número: ")
    
numero = int(numero)
print(par_o_impar(numero))