# Данная программа выводит цвет кармана в игре Рулетка
# по введенному номеру кармана

# Ввести номер кармана
pocket = int(input('Enter the pocket number from 0 to 36: '))

# Узнать цвет введенного кармана
if pocket == 0:
    print('green')
elif pocket >= 1 and pocket <= 10:
    print('black')
elif pocket >= 11 and pocket <=18:
    print('red')
elif pocket >= 19 and pocket <= 28:
    print('black')
elif pocket >= 29 and pocket <= 36:
    print('red')
else:
    print('DENIED! Enter a number from 0 to 36!!!')

