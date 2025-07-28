# Данная программа высчитывает площади двух прямоугольников
# и сравнивает их между собой

# Ввести ширину и высоту первого прямоугольника
width_1 = float(input('Enter the Width of the first rectangle: '))
height_1 = float(input('Enter the Height of the first rectangle: '))

# Ввести ширину и высоту второго прямоугольника
width_2 = float(input('Enter the Width of the second rectangle: '))
height_2 = float(input('Enter the Height of the second rectangle: '))

# Расчет площадей прямоугольников
area_1 = width_1 * height_1
area_2 = width_2 * height_2

if area_1 > area_2:
    print('The area of the first rectangle is larger than the' +
        ' area of second rectangle')
elif area_1 < area_2:
    print('The area of the second rectangle is larger than the' +
        ' area of first rectangle')
else:
    print('The areas of the rectangles are equal!')
    