# Данная программа узнает, является ли ваша дата рождения
# магическим числом (произведение дня и месяца равна году)

print('Enter the date of birth if the format dd/mm/yy')

# Ввести дату
day = int(input('Enter the day: '))
month = int(input('Enter the month: '))
year = int(input('Enter the year(The last two digits): '))

# Вывести дату
print(f'Date of birth - {day:02d}.{month:02d}.{year:02d}')

# Рассчитать произведение дня и месяца
mult = day * month

# Узнать, магическое ли число
if mult == year:
    print('Date of birth - MAGIC NUMBER!!!')
else:
    print('Not a magic number')
