import turtle

turtle.shape('turtle')
print('Сколько лап?')
n=int(input())
corner=360/n
for a in range(0,360,int(corner)):
    turtle.right(corner)
    turtle.forward(250)
    turtle.stamp()
    turtle.backward(250)


