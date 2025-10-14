#Crea un módulo llamado operaciones que contenga cuatro funciones básicas relacionadas con operaciones numéricas:
# suma(a, b) → devuelve la suma de dos números.
# resta(a, b) → devuelve la resta de dos números.
# multiplicacion(a, b) → devuelve la multiplicación de dos números.
# division(a, b) → devuelve la división de dos números (controlando la división entre cero).
#Crea un programa principal main.py que y importe el módulo matemáticas, pida al usuario
#dos números y muestre los resultados de aplicar cada una de las funciones anteriores.

import operaciones as op

def main():
    a = float(input("Introduce el primer número: "))
    b = float(input("Introduce el segundo número: "))

    print("\nResultados:")
    print(f"Suma: {op.suma(a, b)}")
    print(f"Resta: {op.resta(a, b)}")
    print(f"Multiplicación: {op.multiplicacion(a, b)}")
    print(f"División: {op.division(a, b)}")

if __name__ == "__main__":
    main()