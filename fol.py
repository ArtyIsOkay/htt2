import turtle

#turtle.tracer(0)
turtle.speed(10)
turtle.pensize(6)
turtle.bgcolor('black')
turtle.pencolor('gold')

#Задаем начальную позицию черепахи
turtle.penup()
turtle.left(220)
turtle.forward(550)
turtle.right(220)

#Функция, рис2у0ющая ряд из заданного количества кругов вниз
def circledown(x):
    for i in range(x):
        turtle.pendown()
        turtle.circle(100)
        turtle.penup()
        turtle.right(90)
        turtle.forward(100)
        turtle.left(90)

#Функция, смещающая следующий ряд кругов вправо
def position(y):
    turtle.forward(86)
    turtle.left(90)
    turtle.forward(y)
    turtle.right(90)

#Функция для автоматизации отрисовки 
def auto_draw(steps):
    for offset, count in steps:
        position(offset)
        circledown(count)

pattern = [(450, 5), (550, 6), (650, 7), 
           (750, 8), (850, 9), (850, 8), 
           (750, 7), (650, 6), (550, 5)]

auto_draw(pattern)

turtle.update()
turtle.exitonclick()