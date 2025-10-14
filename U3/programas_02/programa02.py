#Modifica el programa anterior para que solo se importen las funciones del módulo math
#que se usan en el programa.

from math import sin, cos, radians, sqrt, pow

print("1. Seno de un ángulo")
print("2. Coseno de un ángulo")
print("3. Raíz cuadrada de un número")
print("4. Potencia de dos números")

opcion = int(input("Selecciona la opción: "))

if opcion == 1:
    angulo = float(input("Ingrese el ángulo en grados: "))
    resultado = sin(radians(angulo))
    print(f"El seno de {angulo}° es: {resultado}")

elif opcion == 2:
    angulo = float(input("Ingrese el ángulo en grados: "))
    resultado = cos(radians(angulo))
    print(f"El coseno de {angulo}° es: {resultado}")

elif opcion == 3:
    numero = float(input("Ingrese el número: "))
    if numero < 0:
        print("No se puede calcular la raíz cuadrada de un número negativo.")
    else:
        resultado = sqrt(numero)
        print(f"La raíz cuadrada de {numero} es: {resultado}")

elif opcion == 4:
    base = float(input("Ingrese la base: "))
    exponente = float(input("Ingrese el exponente: "))
    resultado = pow(base, exponente)
    print(f"{base} elevado a la {exponente} es: {resultado}")

else:
    print("Opción no válida. Intente de nuevo.")