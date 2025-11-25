import random

def generar_enemigo():
    nombres = ["Hydra", "Kraken", "Minotauro", "Gorgona", "Titán"]
    nombre = random.choice(nombres)
    conocimiento = random.randint(1,10)
    energia = random.randint(1,5)
    return nombre, conocimiento, energia

def ataque_enemigo(conocimiento, energia):
    return (conocimiento * energia) * random.randint(1,3)

def mostrar_enemigo(nombre, conocimiento, energia):
    print("---------------------")
    print("Enemigo:",nombre)
    print(" -Conocimiento:",conocimiento)
    print(" -Energia",energia)
    print("---------------------")
    print("")