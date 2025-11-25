#Escribe un programa en Python que realice las siguientes operaciones con cadenas
#   Declara dos cadenas y únelas con concatenación (+)
#   Repite una cadena tres veces con *
#   Compara dos cadenas lexicográfficamente en indica cuál es mayor
#   Comprueba si una subcadena pertenece a otra con in

cadena1 = "Hola"
cadena2 = "como estas"
cadena_unida = cadena1 + " " + cadena2

cadena_repetida = ("Hola" *3)

if (cadena1 > cadena2):
    print("Cadena 1 es mayor")
elif (cadena1 < cadena2):
    print("Cadena 2 es mayor")
else:
    print("Son iguales")

if (cadena1 in cadena_unida):
    print("Cadena1 es una subcadena de candena unida")