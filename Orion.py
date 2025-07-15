import turtle

#turtle.tracer(0)
turtle.hideturtle()
turtle.setup(1000, 1200)
turtle.bgcolor('black')
turtle.pencolor('white')
turtle.penup()

#Левое плечо
LEFT_SHOULDER_X = -140
LEFT_SHOULDER_Y = 400
#Правое плечо
RIGHT_SHOULDER_X = 160
RIGHT_SHOULDER_Y = 360
#Пояс лево
LEFT_BELT_X = -80
LEFT_BELT_Y = -40
#Пояс центр
MIDDLE_BELT_X = 0
MIDDLE_BELT_Y = 0
#Пояс право
RIGHT_BELT_X = 80
RIGHT_BELT_Y = 40
#Левое колено
LEFT_KNEE_X = -180
LEFT_KNEE_Y = -360
#Правое колено
RIGTH_KNEE_X = 240
RIGTH_KNEE_Y = -280

#Нанесем точки звезд
turtle.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y) #Бетельгейзе
turtle.dot()
turtle.goto(RIGHT_SHOULDER_X, RIGHT_SHOULDER_Y) #Хатиса
turtle.dot()
turtle.goto(LEFT_BELT_X, LEFT_BELT_Y) #Альнитак
turtle.dot()
turtle.goto(MIDDLE_BELT_X, MIDDLE_BELT_Y) #Альнилам
turtle.dot()
turtle.goto(RIGHT_BELT_X, RIGHT_BELT_Y) #Минтака
turtle.dot()
turtle.goto(LEFT_KNEE_X, LEFT_KNEE_Y) #Саиф
turtle.dot()
turtle.goto(RIGTH_KNEE_X, RIGTH_KNEE_Y) #Ригель
turtle.dot()

#Нанесем названия звезд
turtle.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y) #Бетельгейзе
turtle.write('Бетельгейзе')
turtle.goto(RIGHT_SHOULDER_X, RIGHT_SHOULDER_Y) #Хатиса
turtle.write('Хатиса')
turtle.goto(LEFT_BELT_X, LEFT_BELT_Y) #Альнитак
turtle.write('Альнитак')
turtle.goto(MIDDLE_BELT_X, MIDDLE_BELT_Y) #Альнилам
turtle.write('Альнилам')
turtle.goto(RIGHT_BELT_X, RIGHT_BELT_Y) #Минтака
turtle.write('Минтака')
turtle.goto(LEFT_KNEE_X, LEFT_KNEE_Y) #Саиф
turtle.write('Саиф')
turtle.goto(RIGTH_KNEE_X, RIGTH_KNEE_Y) #Ригель
turtle.write('Ригель')

#Соединим все звезда в созвездие
#От левого плеча к левому поясу
turtle.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y) #Бетельгейзе
turtle.pendown()
turtle.goto(LEFT_BELT_X, LEFT_BELT_Y) #Альнитак
turtle.penup()

#От левого колена к левому поясу
turtle.goto(LEFT_KNEE_X, LEFT_KNEE_Y) #Саиф
turtle.pendown()
turtle.goto(LEFT_BELT_X, LEFT_BELT_Y) #Альнитак
turtle.penup()

#От правого плеча к правому поясу
turtle.goto(RIGHT_SHOULDER_X, RIGHT_SHOULDER_Y) #Хатиса
turtle.pendown()
turtle.goto(RIGHT_BELT_X, RIGHT_BELT_Y) #Минтака
turtle.penup()

#От правого колена к правому поясу
turtle.goto(RIGTH_KNEE_X, RIGTH_KNEE_Y) #Ригель
turtle.pendown()
turtle.goto(RIGHT_BELT_X, RIGHT_BELT_Y) #Минтака
turtle.penup()

#Пояс Ориона левый
turtle.goto(LEFT_BELT_X, LEFT_BELT_Y) #Альнитак
turtle.pendown()
turtle.goto(MIDDLE_BELT_X, MIDDLE_BELT_Y) #Альнилам
turtle.penup()

#Пояс Ориона правый
turtle.goto(RIGHT_BELT_X, RIGHT_BELT_Y) #Минтака
turtle.pendown()
turtle.goto(MIDDLE_BELT_X, MIDDLE_BELT_Y) #Альнилам
turtle.penup()

turtle.exitonclick()