#Mejora el programa anterior de forma que compruebe si el usuario está introduciendo
#valores correctos (por ejemplo, el radio no puede ser un número negativo) y si no es así
#que pida muestre un aviso y vuelva a pedir el valor


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
            print("Saliendo del programa")
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
    while True:
        try:
            radio = float(input("Introduce el radio del círculo: "))
            if radio > 0:
                area = calcular_area_circulo(radio)
                print(f"El área del círculo es: {area:.2f}")
                break
            else:
                print("El radio debe ser mayor que 0")
        except ValueError:
            print("Valor no válido")

def opcion2():
    while True:
        try:
            base = float(input("Introduce la base del triángulo: "))
            altura = float(input("Introduce la altura del triángulo: "))
            if base > 0 and altura > 0:
                area = calcular_area_triangulo(base, altura)
                print(f"El área del triángulo es: {area:.2f}")
                break
            else:
                print("Base y altura deben ser mayores que 0")
        except ValueError:
            print("Valor no válido")

def opcion3():
    while True:
        try:
            base = float(input("Introduce la base del rectángulo: "))
            altura = float(input("Introduce la altura del rectángulo: "))
            if base > 0 and altura > 0:
                area = calcular_area_rectangulo(base, altura)
                print(f"El área del rectángulo es: {area:.2f}")
                break
            else:
                print("Base y altura deben ser mayores que 0")
        except ValueError:
            print("Valor no válido")

if __name__ == "__main__":
    main()