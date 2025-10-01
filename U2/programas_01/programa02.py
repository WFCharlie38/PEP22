#Escribe un programa que pida primero un número par (positivo o negativo) y si el valor no es correcto, muestre un aviso. 
# Si el valor es correcto, pedirá un número impar (positivo o negativo) y si el valor no es correcto, mostrará un aviso.

numpar = int(input("Introduce un número par: "))
if numpar % 2 == 0:
    numimpar = int(input("Introduce un número impar: "))
    if numimpar % 2 == 0:
        print("Error, has introducido un número incorrecto")
else:
    print("Error, has introducido un número incorrecto")



