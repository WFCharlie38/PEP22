#Escribe un programa que dado un número de dos cifras, diseñe un algoritmo que permita obtener el número invertido.

numero = int(input("Introduce un número de dos cifras: "))

decenas = numero // 10    
unidades = numero % 10   

numero_invertido = (unidades * 10) + decenas

print("El número invertido es:", numero_invertido)
