# Программа для смешивания цветов

print('This program mixes colors!\n'
      + 'List of commands:')
print('Red -    r\n'
      + 'Blue -   b\n'
      + 'Yellow - y')

# Ввести два смешиваемых цвета
first_color = str(input('First color: '))
second_color = str(input('Second color: '))

# Получить значение смешивания
mix = first_color + second_color

# Значения цветов после смешивания
purple_1 = 'rb'
purple_2 = 'br'
orange_1 = 'ry'
orange_2 = 'yr'
green_1 = 'by'
green_2 = 'yb'

# Получить и вывести результат смешивания
if mix == purple_1 or mix == purple_2:
    print('If you mix Red and Blue, you get PURPLE')
elif mix == orange_1 or mix == orange_2:
    print('If you mix Red and Yellow, you get ORANGE')
elif mix == green_1 or mix == green_2:
    print('If you mix Blue and Yellow, you get GREEN')
else:
    print('DENIED!!! Please, enter the required command' + 
          '( "r" - for Red, "b" - for Blue, "y" - for Yellow)')

