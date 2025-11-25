#Escribe un programa en Python que realices las siguientes operaciones con cadenas
#   Crea una cadena "Python"
#   Extrae la subcadena "Pyt" con slicing
#   Extrae los caracteres en posicones pares con slciing ::2
#   Invierte la cadena con slicing [::-1]
#   Recorre la cadena carácter por carácter e imprímelos

cadena = "Python"
subcadena = cadena[0:3]
print(subcadena)

caracteres_pares = cadena[::2]
print(caracteres_pares)

cadena_invertida = cadena[::-1]
print(cadena_invertida)

longitud_cadena = len(cadena)
for i in range(longitud_cadena):
    print(cadena[i], end="")