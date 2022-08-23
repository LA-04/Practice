import turtle

turtle.shape('turtle')

def n_square():
    n = 1
    k = 1
    turtle.speed(100000)
    while n <= 10:
        for i in range(1, 360, 1):
            turtle.forward(k)
            turtle.left(1)
        for i in range(1, 360, 1):
            turtle.forward(k)
            turtle.right(1)

        n += 1
        k += 0.1


turtle.speed(100000)
n_square()
