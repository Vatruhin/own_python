#Задача 6: паук
import turtle
turtle.shape('turtle')

n = 10
a = 360 / n
for i in range(n):
    turtle.forward(50)
    turtle.stamp()
    turtle.backward(50)
    turtle.left(a)
