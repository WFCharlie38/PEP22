import json

try:
    with open("paises.json", "r", encoding="utf-8") as archivo:
        paises = json.load(archivo)

    for pais in paises:
        print(f"{pais['nombre']} está en {pais['continente']} y tiene {pais['poblacion']} millones de habitantes.")

except FileNotFoundError:
    print("Error: El archivo 'paises.json' no existe.")

except json.JSONDecodeError:
    print("Error: El archivo no tiene un formato JSON válido.")

except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")
