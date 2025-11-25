import json

capitales = [
    {"país": "Francia", "capital": "París"},
    {"país": "Australia", "capital": "Canberra"},
    {"país": "Kenia", "capital": "Nairobi"},
    {"país": "Brasil", "capital": "Brasilia"}
]

try:
    with open("capitales.json", "w", encoding="utf-8") as archivo:
        json.dump(capitales, archivo, ensure_ascii=False, indent=4)
    print("Archivo 'capitales.json' creado correctamente.")

except Exception as e:
    print(f"Ocurrió un error al crear el archivo: {e}")
