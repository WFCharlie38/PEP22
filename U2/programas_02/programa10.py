#Modifica el programa anterior par que pida en primer lugar el número de jugadores que 
#van a jugar. Cada jugador irá jugando y el programa mostrará si ha ganado o no a la banca.

import random

banca = random.randint(17, 21)
print("La banca ya tiene su jugada (oculta).")

num_jugadores = int(input("Introduce el número de jugadores: "))

for j in range(1, num_jugadores + 1):
    print(f"\n--- Turno del jugador {j} ---")
    jugador = 0

    while True:
        opcion = input("¿Quieres sacar una carta? (s/n): ").lower()
        if opcion != "s":
            break

        carta = random.randint(1, 5)
        jugador += carta
        print(f"Has sacado un {carta}. Total: {jugador}")

        if jugador > 21:
            print("Te pasaste de 21. ¡Pierdes!")
            break

    if jugador <= 21:
        print(f"\nTu puntuación final: {jugador}")
        print(f"Puntuación de la banca: {banca}")
        if jugador > banca:
            print("Has ganado a la banca. ¡Felicidades!")
        else:
            print("Tu puntuación es menor o igual que la banca. ¡Pierdes!")

print("\n--- Fin del juego ---")
print(f"La banca tenía {banca}.")