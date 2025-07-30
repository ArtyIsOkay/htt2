# Эта программа считает количество пачек сосисок и булочек для пикника
# Сосисок в пачке 10 штук, булочек в пачке 8 штук

# Именные константы
SAUSAGE_PER_PACK = 10
BUN_PER_PACK = 8

# Узнать количество участников и количество
# хотдогов для каждого
participans = int(input('Enter the number of participant: '))
hot_dog = int(input('Enter the number of hotdogs per participant: '))

# Узнать общее количесвто хотдогов
hot_dog_total = participans * hot_dog

# Узнать сколько понадобится пачек сосисок
# Узнать сколько сосисок останется
if (hot_dog_total % SAUSAGE_PER_PACK) == 0:
    print(f'Need {hot_dog_total // SAUSAGE_PER_PACK} packs of sausages')
    print('Leftover sausages - 0')
else:
    sausage_packs = (hot_dog_total // SAUSAGE_PER_PACK) + 1
    sausage_leftover = SAUSAGE_PER_PACK - (hot_dog_total % SAUSAGE_PER_PACK)
    print(f'Need {sausage_packs} packs of sausages')
    print(f'Leftover sausages - {sausage_leftover}')

# Узнать сколько понадобится пачек булочек
# Узнать сколько булочек останется
if (hot_dog_total % BUN_PER_PACK) == 0:
    print(f'Need {hot_dog_total // BUN_PER_PACK} packs of bun')
    print('Leftover buns - 0')
else:
    bun_packs = (hot_dog_total // BUN_PER_PACK) + 1
    bun_leftover = BUN_PER_PACK - (hot_dog_total % BUN_PER_PACK)
    print(f'Need {bun_packs} packs of bun')
    print(f'Leftover buns - {bun_leftover}')
