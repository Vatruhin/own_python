#Задача 7: спираль
import turtle

n = 100
a = 180 - (180*(n-2))/n
for i in range(n):
      
    turtle.shape('turtle')
    turtle.forward(5)
    turtle.left(a)


