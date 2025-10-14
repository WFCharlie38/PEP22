def a_binario(n):
    if not isinstance(n, int):
        return "Error: el valor debe ser un número entero."
    return bin(n)[2:]

def a_hexadecimal(n):
    if not isinstance(n, int):
        return "Error: el valor debe ser un número entero."
    return hex(n)[2:]

def a_entero(texto):
    try:
        return int(texto)
    except ValueError:
        return "Error: el texto no representa un número entero válido."
