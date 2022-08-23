import turtle

turtle.shape('turtle')

def n_square(stars):
    line = 100
    for i in range(stars):
        turtle.forward(line)
        turtle.right(180 - 360 / stars / 2)

n_square(int(input()))