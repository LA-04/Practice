import turtle
from random import *

a, b = 0, 0

turtle.shape("turtle")

for i in range(100):
    turtle.forward(randint(10, 50))
    turtle.right(randint(1, 360))
    turtle.forward(randint(10, 50))
    turtle.left(randint(1, 360))

