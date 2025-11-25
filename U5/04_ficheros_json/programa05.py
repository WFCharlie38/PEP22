import json

try:
    with open("paises.json", "r", encoding="utf-8") as archivo:
        paises = json.load(archivo)

    continente_buscar = input("Introduce un continente: ").strip()

    paises_filtrados = [
        pais for pais in paises
        if pais["continente"].lower() == continente_buscar.lower()
    ]

    if paises_filtrados:
        print("\nPaíses encontrados:")
        for pais in paises_filtrados:
            print(f"- {pais['nombre']}")
    else:
        print("No se encontraron países en ese continente.")

    with open("paises_filtrados.json", "w", encoding="utf-8") as archivo_salida:
        json.dump(paises_filtrados, archivo_salida, ensure_ascii=False, indent=4)

    print("\nArchivo 'paises_filtrados.json' creado correctamente.")

except FileNotFoundError:
    print("Error: El archivo 'paises.json' no existe.")

except json.JSONDecodeError:
    print("Error: El archivo no tiene un formato JSON válido.")

except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")
