import json

pais = {
    "nombre": "Islandia",
    "capital": "Reikiavik",
    "idiomas": ["Islandés", "Inglés"],
    "superficie_km2": 103000
}

cadena_json = json.dumps(pais, indent=2, sort_keys=True, ensure_ascii=False)

print(cadena_json)
