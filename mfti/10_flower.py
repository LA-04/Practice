import turtle

turtle.shape('turtle')

def n_square(circl):
    i = 0
    for i in range(circl):
        p = 0
        while p<360:
            turtle.right(1)
            turtle.forward(1)
            p+=1
        p = 0
        while p<360:
            turtle.left(1)
            turtle.forward(1)
            p+=1
        turtle.left(120)
turtle.speed(1000)
n_square(int(input()))