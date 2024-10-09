# Dos equipos de futbol están disputando el saque inicial del juego. 
# Los capitanes de cada equipo deciden jugar el clásico juego "Piedra, papel o tijera" para definir quien hace el saque. 
# Las reglas son las usuales: Piedra vence a Tijera, Tijera vence a Papel y Papel vence a Piedra.
# Juegan una sola vez.

equipo1 = input("ingrese piedra, papel o tijera: ").lower()
equipo2 = input("ingrese piedra, papel o tijera: ").lower()

win_conditionplayer_1 = (equipo1 == "piedra" and equipo2 == "tijera") or \
    (equipo1 == "tijera" and equipo2 == "papel") or \
    (equipo1 == "papel" and equipo2 == "piedra")


if equipo1 == equipo2:
    print("Empate")
elif win_conditionplayer_1:
    print("gana el equipo 1")
else:
    print("gana el equipo 2") 
 