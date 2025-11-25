import  json

cadena_json = '''
[
{"nombre": "Chile", "moneda": "Peso chileno"},
{"nombre": "Egipto", "moneda": "Libra egipcia"}
]
'''

datos = json.loads(cadena_json)

print("Tipo de dato:", type(datos))

for elemento in datos:
    print(f"{elemento['nombre']} usa la moneda {elemento['moneda']}.")