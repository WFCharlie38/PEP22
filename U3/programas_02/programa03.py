#Escribe un programa que use los módulos platform y os para,
# Mostrar el procesador donde se ejecuta el programa.
# Mostrar el sistema operativo y versión donde se ejecuta el programa.
# Mostrar el nombre el host donde se ejecuta el programa.
# Mostrar el directorio actual.s

import platform
import os

print("Procesador:", platform.processor())

print("Sistema operativo:", platform.system())
print("Versión del sistema:", platform.version())

print("Nombre del host:", platform.node())

print("Directorio actual:", os.getcwd())
