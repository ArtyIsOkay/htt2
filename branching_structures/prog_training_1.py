# Данная программа определяет возрастную категорию
# человека по введенному возрасту в годах

# Ввести возраст пользователя
age = float(input('Enter your age: '))

# Определить возрастную категорию и вывести результат
if age <= 1:
    print('You\'re a baby')
elif age > 1 and age <= 13:
    print('You\'re a child')
elif age > 13 and age <= 20:
    print('You\'re a teenager')
else:
    print('You\'re a adult')
