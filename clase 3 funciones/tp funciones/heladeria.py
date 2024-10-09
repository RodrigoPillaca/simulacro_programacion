COMISION = 50

#Precios
PRECIO_TAMANIO_C = 2000
PRECIO_TAMANIO_M = 3000
PRECIO_TAMANIO_G = 3700

#Calorias de los helados 
CHOCOLATE = 600
GRANIZADO = 750
VAINILLA = 780
DULCE_LECHE = 800

#CONTADORES
contador_tamanio_chico=0
contador_tamanio_medio=0
contador_tamanio_grande=0

# Por compra se ingresa:
# ● Cantidad de gustos (>0 y <=4) VALIDAR LA CANTIDAD DE GUSTOS
# ● Importe a cobrar + Comisión de heladero ($50).
# ● Nombre de quien lo compró.

def validar_tamanio (tamanio : str) -> str:
    """Función que valida si una cadena es "C", "M" o "G" y devuelve la cadena. 
    Argumentos: string
    Returns: string
    """
    tamanio = tamanio.upper()
    while (tamanio!="C") and (tamanio!= "M") and (tamanio!= "G"):
        tamanio = str(input("Incorrecto, ingrese C, M o G: ")).upper()
    return tamanio

def validar_cantidad_gustos (cantidad : int) -> int:
    """"Validamos que la cantidad de gustos ingresados este en el rango 1-4
    arg: int
    return: int
    """
    while not (0 < cantidad <= 4):
        cantidad = int(input("La cantidad de gustos ingresadas debe ser de 1 hasta 4: "))
    return cantidad

def importe_total(tamanio : str) -> float :
    """Funcion que toma un tamaño en str y retorna su precio sumándole una comisión 
    Args: str{tamanio}
    Return :float{importe+comision}
    """
    if tamanio == "C":
        importe = PRECIO_TAMANIO_C
    elif tamanio == "M":
        importe = PRECIO_TAMANIO_M
    else: 
        importe = PRECIO_TAMANIO_G
    return (importe+COMISION)

def propiedades_gustos (cantidad):
    for _ in range(cantidad):
        gusto = (input("Ingrese el gusto que deseé: "))
        while gusto != "dulce de leche" and gusto != "granizado" and gusto != "vainilla" and gusto != "chocolate":
            gusto = input("El gusto ingresado no existe o no se encuentra disponible, ingrese otro gusto: ")
            #hacer de alguna forma: comparar gustos y ordenar de menor a mayor calorias / con un len?
        

while True:
    tamanio = validar_tamanio(input("Ingrese el tamaño: "))
    cantidad_gustos = validar_cantidad_gustos(input("Ingrese la cantidad de gustos: "))
    nombre = input("Ingrese su nombre: ")
    importe_a_cobrar = importe_total(tamanio)
    nombre_del_gusto = input("Ingrese el nombre del gusto: ")
    

    if tamanio == "C":
        contador_tamanio_chico+=1
    elif tamanio == "M":
        contador_tamanio_medio+=1
    else:
        contador_tamanio_grande+=1




# Lote de pruebas
tamanio = input("Decime el tamaño de helado C, M o G: ")
validar_tamanio(tamanio)
cantidad = int(input("Decime cantidad de gustos (1 a 4):"))
validar_cantidad_gustos(cantidad)