import turtle

turtle.shape('turtle')

def n_square(n):
   for how in range(n):

       for i in range(1,360,1):
           turtle.forward(1)
           turtle.left(1)
       for i in range(1, 360, 1):
           turtle.forward(1)
           turtle.right(1)

       turtle.left(240)
       how+=2

turtle.speed(1000)
n_square(int(input()))
