def jugar(jugador1: str, jugador2: str) -> str:
    """Compara dos variables str "Jugador 1" y "Jugador 2". \
    Sigue las reglas de piedra papel o tijera para determinar si gana el jugador 1 o jugador 2. Retorna un str con el mensaje de quién gana"""

    mensaje = ""
    ganador = (jugador1 == "Piedra" and jugador2 == "Tijera") or (jugador1 == "Tijera" and jugador2 == "Papel") or (jugador1 == "Papel" and jugador2 == "Piedra")
    
    # retornamos el ganador
    if jugador1 == jugador2:
        mensaje = "Empate"
    
    elif ganador:
        mensaje = "Gana el jugador 1"

    else:
        mensaje = "Gana el jugador 2"
        
    return mensaje

def mostrar_reglas() -> str:
    """Retorna la variable reglas, que contiene una str con las reglas del piedra papel o tijera"""
    
    reglas= """Ambos jugadores deben elegir entre Piedra, Papel y Tijera.
            La piedra vence a las tijeras.
            Las tijeras vencen al papel y el papel vence a la piedra.
            En caso de empate, vuelven a jugar hasta desempatar"""
    
    return reglas


entrar = True
while entrar: #Condicion de corte
    menu_resutado = int(input("""
    1. Jugar --> se ejecutara la funcion para comenzar el juego
    2. Mostrar las reglas del juego --> tambien sea una funcion
    3. Salir --> terminara el programa selecione 1, 2 o 3: """))
    match menu_resutado:
        case 1:
            jugador1 = input("Jugador 1, elija Piedra, Papel o Tijera: ")
            jugador2 = input("Jugador 2, elija Piedra, Papel o Tijera: ")
            print(jugar(jugador1, jugador2))
        case 2:
            print(mostrar_reglas())
        case 3:
            print("no te gustan los juegos kpo XD")
            entrar = False
        case _:
            print("Error: Ingrese una opción válida.")