# Игра "Попади в цель"
import turtle

# Константы
SCREEN_WIDTH = 600      #Ширина экрана
SCREEN_HEIGHT = 600     #Высота экрана
TARGET_LEFT_X = 100     #Левая нижняя координата цели по Х
TARGET_LEFT_Y = 250     #Левая нижняя координата по Y
TARGET_WIDTH = 25       #Ширина цели
TARGET_HEIGHT = 25      #Высота цели
FORCE_FACTOR = 30       #Фактор произваольной силы
PROJECTILE_SPEED = 1    #Скорость анимации снаряда
NORTH = 90              #Угол северного напрвления
SOUTH = 270             #Угол южного напрвления
EAST = 0                #Угол восточного напрвления
WEST = 180              #Угол западного напрвления

# Настройка окна
turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)

# Нарисовать цель
turtle.hideturtle()
turtle.speed(0)
turtle.penup()
turtle.goto(TARGET_LEFT_X, TARGET_LEFT_Y)
turtle.pendown()
turtle.setheading(EAST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(NORTH)
turtle.forward(TARGET_HEIGHT)
turtle.setheading(WEST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(SOUTH)
turtle.forward(TARGET_HEIGHT)
turtle.penup()

# Центровка черепахи
turtle.goto(0, 0)
turtle.setheading(EAST)
turtle.showturtle()
turtle.speed(PROJECTILE_SPEED)

# Получить параметры выстрела от пользователя
# Угол и силу
print('Игра "Попади в цель:"')
print('Вам нужно ввести угол и силу выстрела!')
angle = float(input("Введите угол выстрела снаряда: "))
force = float(input("Введите силу снаряда (1-10): "))

# Рассчитать расстояние выстрела
distance = force * FORCE_FACTOR

# Задать направление
turtle.setheading(angle)

# Запустить снаряд
turtle.pendown()
turtle.forward(distance)

# Проверка на порадение цели
if (turtle.xcor() >= TARGET_LEFT_X and
    turtle.xcor() <= (TARGET_LEFT_X + TARGET_WIDTH) and
    turtle.ycor() >= TARGET_LEFT_Y and
    turtle.ycor() <= (TARGET_LEFT_Y + TARGET_HEIGHT)):
    print('Цель поражена!')
else:
    print('Вы промахнулись!')