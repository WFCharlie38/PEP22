#Escribe un programa en Python que realice las siguientes operaciones con cadenas:
#   Declara variables con tu nombre, curso y año
#   Muestra un mensaje con str.format()
#   Muestra el mismo mensaje usando f-strings
#   Usa un f-string para mostrar el resultado de una operación matemática con dos números

nombre = "Emilio"
curso = "2DAW"
año = "2025/2026"

print("El alumno {} cursa {} en el año {}".format(nombre,curso,año))
print(f"El alumno {nombre} cursa {curso} en el año {año}")
print(f" 2 + 2 = {2 + 2}")