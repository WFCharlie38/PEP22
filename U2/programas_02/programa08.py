#Escribe un programa para jugar a adivinar un número. En primer lugar la aplicación 
#solicita genera un número aleatorio entre 1 y 20. A continuación va pidiendo números y va 
#respondiendo si el número a adivinar es mayor o menor que el introducido. El programa termina cuando se acierta el número.
#Puedes generar el número usando la función random.randrange(1, 21) para 
#obtener un número aleatorio entre 1 y 20 (para ello debes poner import random al inicio del programa).
#Mejora el programa de forma que el usuario tenga solo 3 intentos

import random

numero_secreto = random.randrange(1, 21)

print("Adivina el número entre 1 y 20:")

while True:
    intento = int(input("Introduce un número: "))

    if intento == numero_secreto:
        print("¡Felicidades! Has acertado.")
        break
    elif intento < numero_secreto:
        print("El número secreto es mayor.")
    else:
        print("El número secreto es menor.")

        import random

numero_secreto = random.randrange(1, 21)

print("Adivina el número entre 1 y 20. Solo tienes 3 intentos.")

intentos = 0
acertado = False

while intentos < 3:
    intento = int(input(f"Intento {intentos+1}: Introduce un número: "))
    intentos += 1

    if intento == numero_secreto:
        print("¡Felicidades! Has acertado.")
        acertado = True
        break
    elif intento < numero_secreto:
        print("El número secreto es mayor.")
    else:
        print("El número secreto es menor.")

if not acertado:
    print(f"Has agotado tus intentos. El número era {numero_secreto}.")
