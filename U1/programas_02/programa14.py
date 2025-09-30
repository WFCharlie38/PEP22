#Escribe un programa que reciba un número de bytes y muestre por pantalla cuantos GBytes, MBytes, KBytes y Bytes son. Tanto para el sistema decimal como el binario.

bytes_totales = int(input("Introduce la cantidad de bytes: "))

gb_decimal = bytes_totales / 1_000_000_000
mb_decimal = bytes_totales / 1_000_000
kb_decimal = bytes_totales / 1_000
b_decimal = bytes_totales

gb_binario = bytes_totales / (1024 ** 3)
mb_binario = bytes_totales / (1024 ** 2)
kb_binario = bytes_totales / 1024
b_binario = bytes_totales

print("\nSistema decimal:")
print(f"{bytes_totales} bytes = {gb_decimal:.2f} GB")
print(f"{bytes_totales} bytes = {mb_decimal:.2f} MB")
print(f"{bytes_totales} bytes = {kb_decimal:.2f} KB")
print(f"{bytes_totales} bytes = {b_decimal} B")

print("\nSistema binario:")
print(f"{bytes_totales} bytes = {gb_binario:.2f} GiB")
print(f"{bytes_totales} bytes = {mb_binario:.2f} MiB")
print(f"{bytes_totales} bytes = {kb_binario:.2f} KiB")
print(f"{bytes_totales} bytes = {b_binario} B")
