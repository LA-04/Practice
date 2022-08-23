import turtle
import math

turtle.shape('turtle')

def n_square(number_of_polygons):
    i, number_side, radius, fw = 3, 3, 10, 10
    if number_of_polygons > 0:
        turtle.penup()
        turtle.forward(radius)
        turtle.pendown()
        for i in range(number_of_polygons):
            p = 0
            angle = ((180 * (number_side - 2) / number_side) / 2)
            turtle.left(180 - angle)
            sin = math.sin(math.pi / number_side)
            side = 2 * radius * sin
            while p < number_side:
                turtle.forward(side)
                turtle.left(360 / number_side)
                p += 1

            turtle.right(360 / number_side)
            turtle.right(angle)
            turtle.penup()
            turtle.forward(fw)
            turtle.pendown()
            number_side += 1
            radius += 10

n_square(int(input()))
