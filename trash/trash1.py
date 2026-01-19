import turtle
turtle.tracer(0)
pensize = 1
mv = 1

for i in range(5000):
    turtle.pensize(pensize)
    turtle.forward(mv)
    turtle.left(91)
    mv += 1
    

turtle.done()