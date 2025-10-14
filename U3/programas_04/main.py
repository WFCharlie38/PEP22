#Crea un paquete llamado matemáticas que contenga tres módulos:
# operaciones: creado en la práctica anterior.
# figuras: tendrá las siguientes funciones.
#◦ area_rectangulo(base, altura): devuelve el área.
#◦ area_triangulo(base, altura): devuelve el área.
#◦ area_circulo(radio): devuelve el área.
# conversiones.py: tendrá las siguientes funciones
#◦ a_binario(n): devuelve la representación binaria de un número entero en forma de cadena.
#◦ a_hexadecimal(n): devuelve la representación hexadecimal de un número entero en forma de cadena.
#◦ a_entero(texto): convierte una cadena numérica en un entero (controlando errores si el texto no es válido)
#Recuerda que debes incluir el fichero __init__.py aunque esté vacío.
#Crea un programa principal main.py que muestre un menú que permita elegir entre:
# Operaciones matemáticas
# Cálculo de áreas geométricas
#Según la opción elegida, pida al usuario los datos necesarios y muestre el resultado correspondiente

from matematicas import (
    suma, resta, multiplicacion, division,
    area_rectangulo, area_triangulo, area_circulo,
    a_binario, a_hexadecimal, a_entero
)

def menu():
    print("\n===== MENÚ PRINCIPAL =====")
    print("1. Operaciones matemáticas")
    print("2. Cálculo de áreas geométricas")
    print("3. Conversiones numéricas")
    print("0. Salir")
    return input("Elige una opción: ")


def operaciones_matematicas():
    a = float(input("Introduce el primer número: "))
    b = float(input("Introduce el segundo número: "))

    print(f"Suma: {suma(a, b)}")
    print(f"Resta: {resta(a, b)}")
    print(f"Multiplicación: {multiplicacion(a, b)}")
    print(f"División: {division(a, b)}")


def calculo_areas():
    print("\n--- Cálculo de áreas ---")
    print("1. Rectángulo")
    print("2. Triángulo")
    print("3. Círculo")
    opcion = input("Elige una figura: ")

    if opcion == "1":
        base = float(input("Base: "))
        altura = float(input("Altura: "))
        print(f"Área del rectángulo: {area_rectangulo(base, altura)}")
    elif opcion == "2":
        base = float(input("Base: "))
        altura = float(input("Altura: "))
        print(f"Área del triángulo: {area_triangulo(base, altura)}")
    elif opcion == "3":
        radio = float(input("Radio: "))
        print(f"Área del círculo: {area_circulo(radio)}")
    else:
        print("Opción no válida.")


def conversiones_numericas():
    print("\n--- Conversiones numéricas ---")
    print("1. A binario")
    print("2. A hexadecimal")
    print("3. A entero (desde texto)")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        n = int(input("Introduce un número entero: "))
        print(f"Binario: {a_binario(n)}")
    elif opcion == "2":
        n = int(input("Introduce un número entero: "))
        print(f"Hexadecimal: {a_hexadecimal(n)}")
    elif opcion == "3":
        texto = input("Introduce el texto a convertir: ")
        print(f"Entero: {a_entero(texto)}")
    else:
        print("Opción no válida.")


def main():
    while True:
        opcion = menu()
        if opcion == "1":
            operaciones_matematicas()
        elif opcion == "2":
            calculo_areas()
        elif opcion == "3":
            conversiones_numericas()
        elif opcion == "0":
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()