# Escribe un programa que pida dos numero y muestre su división. Se deben tener en cuenta que no se puede dividir por 0 mostrando en ese caso un aviso

num1 = int(input("Introduce un número a dividir: "))
if num1 != 0:
    num2 = int(input("Introduce el número por el que dividir: "))
    if num2 != 0:
        print("La division de2", num1 ,"entre", num2 ,"es", num1/num2 )
    else:
        print("Error, no se puede dividir entre 0")
else:
    print("Error, no se puede dividir entre 0")