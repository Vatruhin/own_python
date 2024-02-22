#Задача 5: больше квадратов
import turtle
b = 1

for i in range(10):
    b += 0.2
    j = 0
    while j <= 3:
        j += 1
        a = (50 * b) - 50
        turtle.shape('turtle')
        turtle.forward(50 * b + a)
        turtle.left(90)
    turtle.penup()
    turtle.goto(-a, -a)
    turtle.pendown()