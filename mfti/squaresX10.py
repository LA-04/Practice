import turtle

turtle.shape('turtle')
x=0
y=0
for side in range(10, 110, 10):
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)
    turtle.left(90)
    x-=5
    y-=5
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
