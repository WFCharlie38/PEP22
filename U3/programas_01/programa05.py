#Escribe un programa donde crees varias funciones y pruebes el ámbito de las variables en Python (globales, no locales y locales)

mensaje_global = "Soy global"

def funcion_local():
    mensaje_local = "Soy local"
    print("Dentro de funcion_local():")
    print("mensaje_local =", mensaje_local) 
    print("mensaje_global =", mensaje_global) 

def funcion_no_local():
    global mensaje_global
    mensaje_global = "He sido modificada globalmente"
    print("Dentro de funcion_no_local():")
    print("mensaje_global =", mensaje_global)

def funcion_anidada():
    mensaje = "Variable de funcion_anidada"
    
    def interna():
        nonlocal mensaje
        mensaje = "Variable modificada desde interna"
        print("Dentro de interna(): mensaje =", mensaje)
    
    print("Antes de llamar a interna(): mensaje =", mensaje)
    interna()
    print("Después de llamar a interna(): mensaje =", mensaje)

print("Valor inicial de mensaje_global:", mensaje_global)

funcion_local()

funcion_no_local()

print("Valor de mensaje_global después de funcion_no_local:", mensaje_global)

funcion_anidada()
