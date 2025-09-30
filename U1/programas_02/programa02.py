#Escribe un programa que
#   Cree una variable que almacene el número entero 6.
#   Muestre por pantalla el tipo del objeto que contiene el número 6, y el tipo del objeto al que apunta la variable (deben ser iguales)
#   Cree otra variable a la que se asigne la primera variable.
#   Muestre por pantalla el tipo del objeto que contiene el número 6 y el tipo del objeto al que apunta la variable (deben ser iguales)
#   Utilice los operadores de identidad (is e is not) para comprobar y mostrar por pantalla que los dos variables apuntan al mismo objeto y por lo tanto a la misma posición de memoria.
#   Asigne la cadena “Hola” a la primera variable.
#   Muestre por pantalla el tipo del objeto que contiene la cadena “Hola” y el tipo del objeto al que apunta la variable (deben ser iguales) (y diferentes al objeto 6).
#   Utilice la función isinstance() para comprobar y mostrar por pantalla que el objeto al que apunta la primera variable es de tipo int y el de la segunda es de tipo str.

var1 = 6

print("Objeto 6:", type(6), "| Variable var1:", type(var1))

var2 = var1

print("Objeto 6:", type(6), "| Variable var2:", type(var2))

print("¿var1 is var2? ->", var1 is var2)
print("¿var1 is not var2? ->", var1 is not var2)

var1 = "Hola"

print("Objeto 'Hola':", type("Hola"), "| Variable var1:", type(var1))

print("¿var1 es int? ->", isinstance(var1, int))
print("¿var1 es str? ->", isinstance(var1, str))
print("¿var2 es int? ->", isinstance(var2, int))
print("¿var2 es str? ->", isinstance(var2, str))
