# Данная программа высчитывает стоимость доставки
# в зависимости от массы пакета

# Именные константы


# Ввести массу пакета
mass = float(input('Enter the package weight(in grams): '))

# Рассчитать ставку за 100г. товара
if mass < 200:
    rate = 150
elif mass >= 200 and mass < 600:
    rate = 300
elif mass >=600 and mass < 1000:
    rate = 400
else:
    rate = 475

# Рассчитать стоимость доставки
shipping_cost = (mass * rate) / 100

# Вывести стоимость доставки
print(f'Стоимость доставки : {shipping_cost:10,.2f} $')
