inventario = [["galletitas", 100, 14]]

def validar_opcion_menu(opcion_elegida: str) -> int:
    while opcion_elegida.isdigit() == False:
        opcion_elegida = input("Error, ingrese una opcion valida: ")
    
    opcion_elegida = int(opcion_elegida)
    while opcion_elegida < 1 or opcion_elegida > 6:
        opcion_elegida = validar_opcion_menu(input("Error, ingrese la respuesta: "))
    return opcion_elegida

def menu_principal() -> int:
    opcion_elegida = input("""
        1 Cargar producto/s.
        2 Buscar producto.
        3 Ordenar inventario.
        4 Mostrar producto más caro y más barato.
        5 Mostrar productos con precio mayor a 15000.
        6 Salir
        
        Respuesta: """)
    
    return validar_opcion_menu(opcion_elegida)    
    
def validar_nombre_producto(nombre_producto: str) -> str:
    while nombre_producto.isdigit() == False:
        nombre_producto = input("Error, ingrese el nombre del producto a agregar: ")
    return nombre_producto

def validar_precio_producto(precio_producto: str) ->int:
    while precio_producto.isdigit() == False:
        precio_producto = input("Error, ingrese un precio valido: ")
    
    precio_producto = int(precio_producto)
    while precio_producto < 1:
        precio_producto = validar_precio_producto(input("Error, ingrese un precio postivo: "))
    return precio_producto

def validar_stock_producto(stock_producto: str):
    while stock_producto.isdigit() == False:
        stock_producto = input("Error, ingrese un stock valido: ")
    
    stock_producto = int(stock_producto)
    while stock_producto < 1:
        stock_producto = validar_stock_producto(input("Error, ingrese un número de stock postivo: "))
    return stock_producto


def cargar_producto(nombre: str, stock: int, precio: int) -> list:
    listaAgregado = []
    listaAgregado.append(nombre)
    listaAgregado.append(stock)
    listaAgregado.append(precio)
    return listaAgregado


def producto_a_buscar(producto: str):
    for i in range(0, len(inventario)):
        if inventario[i][i] == producto:
            return inventario[i]


def ordenar_productos():
    n = len(inventario)

    for i in range(n-1):       # <-- bucle padre
        for j in range(n-1-i): # <-- bucle hijo
            if inventario[j][1] > inventario[j+1][1]:
                inventario[j], inventario[j+1] = inventario[j+1], inventario[j]

    return inventario



while True:     
    opcion_menu = menu_principal()

    print(opcion_menu)
    while opcion_menu == 1:
        nombre = validar_nombre_producto(input("Ingrese el nombre del producto: ").lower())
        precio = validar_precio_producto(input("Ingrese el precio del producto: "))
        stock = validar_stock_producto(input("Ingrese stock del producto: "))
        
        nuevo_producto = cargar_producto(nombre, precio, stock)
        print(f"Nuevo producto añadido al inventario: {nombre}")
        inventario.append(nuevo_producto)
        print(inventario)
        
        opcion_carga_producto = int(input("""
            1 Seguir agregando productos      
            2 Menu principal
            
            respuesta: """))
        if opcion_carga_producto == 1:
            pass
        else:
            opcion_menu = menu_principal()
            
        
    if  opcion_menu == 2:
        if inventario == []:
            print("No hay productos")
        else:
            print(inventario)
            producto_encontrado = producto_a_buscar(input("Ingrese el producto que desea buscar: "))
            print(producto_encontrado)
            
            
    elif opcion_menu == 3:
        productos_ordenados = ordenar_productos()
        print(productos_ordenados)
        
    elif opcion_menu == 4:
        productos_ordenados = len(ordenar_productos())
        print(inventario[productos_ordenados -1])
        print(inventario[productos_ordenados - productos_ordenados])
    
    pregunta = input("desea seguir ingresando datos (si/no): ").lower()
    while pregunta != "si" and pregunta != "no":
        pregunta = input("Error, desea seguir ingresando datos: ").lower()
    if pregunta == "no":
        break
    
    # continuar despues con el codigo

