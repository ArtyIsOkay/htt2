# Данная программа выводит вес тела через массу
# в диапазоне от 100 Н до 500 Н

# Ввести массу тела
mass = float(input('Enter the mass of the BODY in KILOGRAMS: '))

# Рассчитать вес тела
weight = mass * 9.8

# Определить вес в диапазоне
if weight > 500:
    print('The Body is too HEAVY!!!')
elif weight < 100:
    print('The Body is too LIGHT!!!')
else:
    print(f'The Weight of the Body = {weight:.2f} H')
