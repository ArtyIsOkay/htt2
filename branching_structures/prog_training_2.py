# Данная программа конвертирует арабские
# цифры в римские от 1 до 10

# Ввести арабскую цифру
num = float(input('Enter an Arabic number from 1 to 10: '))

# Конвертировать и вывести число
if num == 1:
    print(f'Roman numeral = I')
elif num == 2:
    print(f'Roman numeral  = II')
elif num == 3:
    print(f'Roman numeral  = III')
elif num == 4:
    print(f'Roman numeral  = IV')
elif num == 5:
    print(f'Roman numeral  = V')
elif num == 6:
    print(f'Roman numeral  = VI')
elif num == 7:
    print(f'Roman numeral  = VII')
elif num == 8:
    print(f'Roman numeral  = VIII')
elif num == 9:
    print(f'Roman numeral  = IX')
elif num == 10:
    print(f'Roman numeral  = X')
else:
    print('Enter an integer from 1 to 10')
