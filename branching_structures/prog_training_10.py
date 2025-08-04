# Данная программа высчитывает скидку по колитчетсву
# купленных программных пакетов

# Именные константы
PRICE = 99

# Узнать, сколько программных пакетов было приобретено
packeges = float(input('Введите окличесвто купленных программных пакетов: '))

# Вычислить скидку
if packeges >= 10 and packeges < 20:
    discount = 0.9
elif packeges >= 20 and packeges < 50:
    discount = 0.8
elif packeges >= 50 and packeges < 100:
    discount = 0.7
elif packeges >= 100:
    discount = 0.6
else:
    discount = 1

# Вывести сумму скидки и общую сумму покупки
value = PRICE * packeges                    # Цена без учета скидки
value_discount = value * discount           # Цена с учетом скидки
discount_amount = value - value_discount    # Размер скидки

print(f'Цена: {value:25,.2f} $')
print(f'Ваша скидка: {((1 - discount) * 100):18.0f} %')
print(f'Размер скидки: {discount_amount:16,.2f} $')
print(f'Цена со скидкой: {value_discount:14,.2f} $')