#Escribe un programa que pida números hasta que se introduzca un cero. Debe imprimir la 
#suma y la media de todos los números introducidos. Realiza dos versiones: una que utiliza 
#la instrucción break y otra no.ç

suma = 0
contador = 0

while True:
    num = int(input("Introduce un número (0 para salir): "))
    if num == 0:
        break
    suma += num
    contador += 1

if contador > 0:
    media = suma / contador
    print(f"Suma: {suma}, Media: {media}")
else:
    print("No se introdujeron números.")
