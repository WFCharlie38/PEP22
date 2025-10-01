#Escribe un programa que pida dos números y que indique cuál es el menor, cuál el mayor o que indique que son iguales.

num1 = int(input("Introduce un número: "))
num2 = int(input("Introduce el número: "))

if num1 < num2:
    print("El número menor es:", num1, "y el mayor es", num2)
elif num2 < num1:
    print("El número menor es:", num2, "y el mayor es", num1)
else:
    print("Los números son iguales")