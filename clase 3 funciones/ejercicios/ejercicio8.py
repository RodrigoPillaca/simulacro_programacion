# Escribe una función llamada calculo_de_imc que reciba una altura y el peso
# e indique el indice de masa CORPORAL (IMC) de una persona.
# Peso inferior al normal	imc < de 18.5
# Normal imc entre 18.5 – 24.9
# Peso superior al normal  imc entre 25.0 – 29.9
# Obesidad	imc > de 30.0


def calculo_de_imc(imc: float) -> str:

    if imc < 18.5:
        return "Peso inferior al normal"
    elif imc < 24.9:
        return "Peso normal"
    elif imc < 29.9:
        return "Peso superior al normal"
    elif imc > 30.0:
        return "Obesidad"

peso = float(input("ingrese su peso: "))
altura = float(input("ingrese su altura: "))
imc = int(peso / altura**2)

resultado = calculo_de_imc(imc)
print(resultado)

