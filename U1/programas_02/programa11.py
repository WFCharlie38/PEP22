#Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. El tiempo de viaje hasta llegar a otra ciudad B es de N segundos. Escribie un programa que
#determine la hora de llegada a la ciudad B.

horas = int(input("Introduce la hora de salida (HH): "))
minutos = int(input("Introduce los minutos de salida (MM): "))
segundos = int(input("Introduce los segundos de salida (SS): "))

tiempo_viaje = int(input("Introduce el tiempo de viaje en segundos (N): "))

salida_total_segundos = horas * 3600 + minutos * 60 + segundos

llegada_total_segundos = salida_total_segundos + tiempo_viaje

hora_llegada = (llegada_total_segundos // 3600) % 24
minuto_llegada = (llegada_total_segundos % 3600) // 60
segundo_llegada = llegada_total_segundos % 60

print(f"Hora de llegada a la ciudad B: {hora_llegada:02d}:{minuto_llegada:02d}:{segundo_llegada:02d}")
