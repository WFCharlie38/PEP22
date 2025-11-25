#Escribe un programa en Python que realice las sisguientes operaciones con cadenas:
#   Declara una cadena " Hola Mundo"
#   Aplica y muestra los resultados de: upper(), lower(), capitalize(), tittle()
#   Elimina espacios con strip()
#   Sustituye "Mundo" por "Python" con replace()
#   Divide la cadena en palabras con split()
#   Une una lista de palabras con join()

cadena = "Hola Mundo"

print(cadena, cadena.upper())
print(cadena, cadena.lower())
print(cadena, cadena.capitalize())
print(cadena, cadena.title())

print(cadena, cadena.strip())

print(cadena, cadena.replace("Mundo","Python"))

cadena_divida = cadena.split(cadena)

cadena_unida = " ".join(cadena_divida)
print(cadena_unida)