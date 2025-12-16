import random

# Лого игры
print("=" * 54)
print("                 КИНЬ")
print("                       игра")
print("                             КУБИКИ!")
print("=" * 54)
print(f"""\nДва игрока по очереди бросают по 3 кубика и побеждает 
            игрок с бОльшим значением""")

# Значение для повторной игры
contin = "д"

while contin == 'д':
    first_player = input('\nИгрок 1, нажмите Enter чтобы бросить кубики')
    a = random.randint(1, 6)
    b = random.randint(1, 6)
    c = random.randint(1, 6)
    res_1 = a + b + c
    print(f'Игрок 1 бросил кубики и вот результаты:')
    print(f"""    Кубик 1 = {a}
    Кубик 2 = {b}
    Кубик 3 = {c}
    Общий счет = {res_1}""")

    second_player = input('Игрок 2, нажмите Enter чтобы бросить кубики')
    d = random.randint(1, 6)
    f = random.randint(1, 6)
    g = random.randint(1, 6)
    res_2 = d + f + g
    print(f'Игрок 2 бросил кубики и вот результаты:')
    print(f"""    Кубик 1 = {d}
    Кубик 2 = {f}
    Кубик 3 = {g}
    Общий счет = {res_2}\n""")
    
    if res_1 > res_2:
        print("Побеждает Игрок 1!!!")
    elif res_2 > res_1:
        print("Побеждает Игрок 2!!!")
    else:
        print("ОГО!!! Да это же ничья!!!")
    contin = input("Введите 'д' чтобы начать заново: ")
