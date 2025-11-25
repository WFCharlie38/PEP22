entero = (int)(input("Introduce un número entero: "))
decimal = (float)(input("Introduce un número decimal: "))
cadena = input("Introduce una cadena de texto: ")

print(entero, type(entero))
print(decimal, type(decimal))
print(cadena, type(cadena))

es_entero = isinstance(entero, int)
es_decimal = isinstance(decimal,float)
es_cadena = isinstance(cadena,str)

comprobaciones = es_entero and es_decimal and es_cadena
print(comprobaciones)