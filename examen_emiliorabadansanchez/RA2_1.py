import random

vida_jugador = int(3)
puntos_jugador = int(0)
nivel_jugador = int(1)
puntos_nivel = int(0)

while (vida_jugador > 0): 
    try:
        #Impresion de las estadísticas actuales del jugdador
        print("Vida actual:",vida_jugador)
        print("Nivel actual:",nivel_jugador)
        print("Experiencia actual:",puntos_nivel,"/3")

        #Control del tipo de ataque, respecto a ello sacar la carta respectiva del jugador y del enemigo
        print("Elige un ataque: \n -Fuerza 1 \n -Precisión 2 \n -Riesgo 3")
        ataque = int(input(""))

        match ataque:
            case 1:
                carta_jugador = random.randint(5,10)
                carta_enemigo = random.randint(3,10)
                tipo_ataque = "fuerza"
            case 2:
                carta_jugador = random.randint(3,8)
                carta_enemigo = random.randint(2,9)
                tipo_ataque = "precisión"
            case 3:
                carta_jugador = random.randint(1,10)
                carta_enemigo = random.randint(1,8)
                tipo_ataque = "riesgo"
            case _:
                raise ValueError("El valor debe estar entre 1 y 3.")
        
        #Impresion de la jugada, la carta del jugador, la carta del enemigo, comprobación de quien ha ganado a quien y asignacion de puntos y vida
        print("")
        print("--------------------------------------------")
        print("Tu carta:",carta_jugador)
        print("Carta del enemigo:",carta_enemigo)
        if (carta_jugador > carta_enemigo):
            puntos_jugador = puntos_jugador+1
            puntos_nivel = puntos_nivel+1
            print("Has ganado al enemigo usando",tipo_ataque,".\nGanas un punto")
        elif (carta_jugador < carta_enemigo):
            vida_jugador = vida_jugador-1
            print("Has perdido contra el enemigo usando",tipo_ataque,".\nPierdes una vida")
        else:
            print("Has quedado empate con el enemigo, por lo tanto no occure nada")
        print("--------------------------------------------")
        
        #Control de niveles del jugador, por cada 3 puntos sube un nivel, recupera vida siempre que no tenga el maximo 
        #y se reinicia el contador de puntos nivel.
        if (puntos_nivel == 3):
            puntos_nivel = 0
            print("Has subido de nivel")
            nivel_jugador = nivel_jugador+1
            if (vida_jugador < 3):
                vida_jugador = vida_jugador+1
                print("Recuperas vida por subida de nivel")

    except ValueError as e:        
        print("Error:", e)

#Impresion final, despúes de haber perdido todas las vidas
print("")
print("--------------------------------------------")
print("Has perdido todas las vidas")
print("Puntuación final:",puntos_jugador)
print("Nivel alcanzado:",nivel_jugador)
print("--------------------------------------------")