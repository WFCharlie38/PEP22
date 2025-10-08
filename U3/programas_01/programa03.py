#Escribe un programa en Python que muestre un menú que permita al usuario seleccionar
#qué operación desea realizar. Las operaciones que puede realizar serán calcular el área
#de un círculo, un triángulo o un rectángulo. El menú que se le muestra al usuario será similar al siguiente:
#   1. Calcular el área de un círculo
#   2. Calcular el área de un triángulo
#   3. Calcular el área de un rectángulo
#   4. Salir
#Introduce una opción (1-4):
#El programa se estará ejecutando de forma indefinida hasta que el usuario seleccione la opción 4.

import math

def main():
    while True:
        mostrar_menu()
        opcion = input("Introduce una opción (1-4): ")
        if opcion == "1":
            opcion1()
        elif opcion == "2":
            opcion2()
        elif opcion == "3":
            opcion3()
        elif opcion == "4":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Debes introducir un número entre 1 y 4.")

def mostrar_menu():
    print("\n--- MENÚ DE OPERACIONES ---")
    print("1. Calcular el área de un círculo")
    print("2. Calcular el área de un triángulo")
    print("3. Calcular el área de un rectángulo")
    print("4. Salir")

def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_area_triangulo(base, altura):
    return (base * altura) / 2

def calcular_area_rectangulo(base, altura):
    return base * altura

def opcion1():
    radio = float(input("Introduce el radio del círculo: "))
    print(f"El área del círculo es: {calcular_area_circulo(radio):.2f}")

def opcion2():
    base = float(input("Introduce la base del triángulo: "))
    altura = float(input("Introduce la altura del triángulo: "))
    print(f"El área del triángulo es: {calcular_area_triangulo(base, altura):.2f}")

def opcion3():
    base = float(input("Introduce la base del rectángulo: "))
    altura = float(input("Introduce la altura del rectángulo: "))
    print(f"El área del rectángulo es: {calcular_area_rectangulo(base, altura):.2f}")

if __name__ == "__main__":
    main()