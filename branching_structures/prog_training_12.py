# Программа высчитывает индекс массы тела человека

# Именные константы
LOW_LIMIT = 18.5       # Недостаточный вес
HIGH_LIMIT = 25        # Избыточный вес

# Ввести параметры пользователя
height = float(input('Enter your height(in meters): '))
weight = float(input('Enter your weight(in kilo): '))

# Вычислить индекс массы тела
index = weight / (height)**2

# Вывести результаты
if index < 18.5:
    print(f'Your body mass index : {index:.2f}')
    print(f'You are underweight!!!')
elif index >= 18.5 and index <= 25:
    print(f'Your body mass index : {index:.2f}')
    print(f'Is your weigth optimal!!!')
elif index > 25:
    print(f'Your body mass index : {index:.2f}')
    print(f'You are overweight!!!')
else:
    print('DENIED! Inter your height(meters)' + 
          'and weight(kilo)')