#Sabiendo que 1 milla equivale a 1,61 Km escribe un programa que pida un número de millas y un número de Km, muestre respectivamente el número de millas y kilómetros. 
# Los resultados deben estar redondeados a 2 decimales.

millas = float(input("Introduce el número de millas: "))
kilometros = float(input("Introduce el número de kilómetros: "))

millas_a_km = millas * 1.61
km_a_millas = kilometros / 1.61

print(f"{millas} millas equivalen a {millas_a_km:.2f} kilómetros")
print(f"{kilometros} kilómetros equivalen a {km_a_millas:.2f} millas")
