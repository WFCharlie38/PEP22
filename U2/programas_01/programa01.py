#Escribe un programa que pida primero un número par y luego un número impar (positivos o negativos). En caso de que uno o los dos valores no sea correcto 
# (es decir no sea par o impar respectivamente), se mostrará un aviso.

numpar = int(input("Introduce un número par: "))

numimpar = int(input("Introduce un número impar: "))

if numpar % 2 != 0 or numimpar % 2 == 0:
    print("Error, has introducido un número incorrecto")
