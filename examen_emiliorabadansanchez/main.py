from batalla import (
    ataque_jugador, mostrar_jugador,
    generar_enemigo, ataque_enemigo, mostrar_enemigo
)


print("=== BATALLA DE MAGIA ===")
nombre_jugador = str(input("Introduce tu nombre:"))
conocimiento_jugador = int(input("Introduce tu conocimiento (1-10):"))
energia_jugador = int(input("Introduce tu energia (1-5):"))
ronda = 1

nombre_enemigo, conocimiento_enemigo, energia_enemigo = generar_enemigo()

mostrar_jugador(nombre_jugador, conocimiento_jugador, energia_jugador)
mostrar_enemigo(nombre_enemigo, conocimiento_enemigo, energia_enemigo)

while (ronda < 4): 
        magia_jugador = ataque_jugador(conocimiento_jugador, energia_jugador)
        magia_enemigo = ataque_enemigo(conocimiento_enemigo, energia_enemigo)

        print(f"--- RONDA{ronda} ---")
        print(f"Magia de {nombre_jugador}: {magia_jugador}")
        print(f"Magia de {nombre_jugador}: {magia_enemigo}")

        if (magia_jugador > magia_enemigo):
            print(f"{nombre_jugador} lanza un poderoso hechizo (-1 de energia enemigo)")
            energia_enemigo = energia_enemigo-1
        elif (magia_jugador < magia_enemigo):
            print(f"{nombre_jugador} lanza un poderoso hechizo (-1 de energia jugador)")
            energia_jugador = energia_jugador-1
        else:
            print("Ambos ha lanzado un hechizo de la misma potencia, por lo tanto nadie pierde energía")
            print("")
        ronda = ronda+1

print("=== FIN DEL DUELO ===")
if (energia_jugador > energia_enemigo):
    print(f"{nombre_jugador} ha vencido a {nombre_enemigo}")
elif (energia_jugador < energia_enemigo):
    print(f"{nombre_enemigo} ha vencido a {nombre_jugador}")
else:
    print(f"{nombre_jugador} y {nombre_jugador} han quedado empate")