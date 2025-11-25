#Escribe un programa que pida un número y muestre una lista de números desde 1 al 
#número. Se debe controlar que el número no se menor que 1 ni mayor que 10, si es así se 
#pedirá que si introduzca de nuevo, y así hasta que se introduzca el número correcto. 
#Controla las posibles excepciones a la hora de introducir el número por teclado.

try:
    num = int(input("Introduce un número entre 1 y 10: "))
    if num < 1 or num > 10:
        raise ValueError("El número debe estar entre 1 y 10.")
    print(f"Has introducido el número {num}.")
    for i in range(1, num + 1):
        print(i)
except ValueError as e:
    print("Error:", e)