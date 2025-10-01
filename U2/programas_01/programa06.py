#Escribe un programa que pida una fecha (día, mes y año) y diga si es correcta


dia = int(input("Introduce el día: "))
mes = int(input("Introduce el mes: "))
año = int(input("Introduce el año: "))

valida = False

match mes:
    case 1 | 3 | 5 | 7 | 8 | 10 | 12:   
        if 1 <= dia <= 31:
            valida = True
    case 4 | 6 | 9 | 11:                
        if 1 <= dia <= 30:
            valida = True
    case 2:                             
        if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
            if 1 <= dia <= 29:
                valida = True
        else:
            if 1 <= dia <= 28:
                valida = True
    case _:                         
        valida = False

if valida:
    print("La fecha es correcta")
else:
    print("La fecha es incorrecta")
