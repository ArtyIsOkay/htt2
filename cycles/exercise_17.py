# Программа рисует черепахой узор из 100 квадратов

import turtle

turtle.tracer(0)
turtle.hideturtle()

START_X = 250
START_Y = -250
ANGLE = 90
MOVE = 5
SQUARES = 100
OFFSET = 5

# Задать начальное положение
turtle.penup()
turtle.goto(START_X, START_Y)
turtle.left(90)
turtle.pendown()

# Отрисовать квадраты
for i in range(1, SQUARES + 1):
    MOVE += OFFSET
    for j in range(4):
        turtle.forward(MOVE)
        turtle.left(ANGLE)
    turtle.penup()
    turtle.goto(START_X, START_Y)
    turtle.pendown()

turtle.done()
