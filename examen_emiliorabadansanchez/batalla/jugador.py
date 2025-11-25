import random

def ataque_jugador(conocimiento, energia):    
    return (conocimiento * energia) * random.randint(1,3)

def mostrar_jugador(nombre, conocimiento, energia):
    print("---------------------")
    print("Jugador:",nombre)
    print(" -Conocimiento:",conocimiento)
    print(" -Energia",energia)
    print("---------------------")
    print("")