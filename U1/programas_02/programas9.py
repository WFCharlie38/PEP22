#Escribe un programa que calcule la calificación de estudiante en un módulo. La calificación se obtiene de la calificación parcial en cada RA (RA1 20%, RA2, 60% y RA3 20%)

ra1 = float(input("Introduce la calificación de RA1 (0-10): "))
ra2 = float(input("Introduce la calificación de RA2 (0-10): "))
ra3 = float(input("Introduce la calificación de RA3 (0-10): "))

nota_final = (ra1 * 0.20) + (ra2 * 0.60) + (ra3 * 0.20)

print("La calificación final del módulo es:", nota_final)
