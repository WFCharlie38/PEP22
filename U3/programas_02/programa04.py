#El módulo turtle es una biblioteca estándar de Python que permite crear gráficos y dibujos
#de manera sencilla, moviendo una “tortuga” virtual por la pantalla. El módulo está instalado
#por defecto en el interprete de Python.
#Investiga la documentación del módulo https://docs.python.org/3/library/turtle.html y
#escribe un programa que:
#• Dibuje un cuadrado rojo sin rellenar.
#• Dibuje un circulo verde rellen

import turtle

turtle.title("Cuadrado y Círculo")
turtle.bgcolor("white")

t = turtle.Turtle()

t.color("red")
for _ in range(4):
    t.forward(100)
    t.right(90)

t.penup()
t.goto(150, 0)
t.pendown()

t.color("green")
t.begin_fill()
t.circle(50)
t.end_fill()

turtle.done()