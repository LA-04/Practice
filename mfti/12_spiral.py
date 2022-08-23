import turtle

turtle.shape('turtle')

def n_square(spiral):
    for i in range(spiral):
        p = 0
        while p < 180:
            turtle.right(1)
            turtle.forward(1)
            p += 1
        p = 0
        while p < 60:
            turtle.right(3)
            turtle.forward(0.5)
            p += 1
turtle.left(90)
turtle.speed(100000)
n_square(int(input()))