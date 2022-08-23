import turtle


def move(number):
    if number == 1:
        t.left(45)
        t.forward(20)
        t.right(135)
        t.forward(40)


t = turtle
t.shape('turtle')
move(int(input()))
