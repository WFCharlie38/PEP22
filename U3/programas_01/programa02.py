#Escribe un programa en Python que haga uso de una función llamada saludar que cumpla los siguientes requisitos:
#   • Entrada: Tiene 4 parámetros de entrada, que serán 4 cadenas de texto: nombre,
#     primer apellido, segundo apellido y curso. El parámetro curso tendrá en la declaración de la función el valor por defecto “2DAW”.
#   • Salida: No tiene parámetros de salida.
#   • Funcionalidad: Imprime por pantalla un mensaje saludando al alumno/a que se haya pasado como parámetro de entrada.
#El programa debe invocar a la función varias veces. En algunas de ellas se tiene que usar el paso de parámetros de forma nominal (con clave valor)

def saludar(nombre, primer_apellido, segundo_apellido, curso="2DAW"):
    print(f"Hola {nombre} {primer_apellido} {segundo_apellido}, bienvenido/a al curso {curso}.")

saludar("Emilio", "Rabadán", "Sanchez")
saludar("Ainhoa", "Fuster", "Prieto", "1DAM")

saludar(nombre="Luis", primer_apellido="Bermejo", segundo_apellido="Lara")
saludar(segundo_apellido="Molina", nombre="Alvaro", primer_apellido="Moya", curso="1DAW")

saludar("Samuel", "Merino", segundo_apellido="Prado", curso="2DAW")
