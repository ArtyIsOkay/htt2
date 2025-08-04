# Программа преобразует секунды в минуты,
# часы и дни

# Именные константы
MIN = 60        # секунд в минуте
HOUR = 3600     # секунд в часе
DAY = 86400     # секунд в дне

# Внести количество секунд
sec = int(input('Enter the seconds: '))

# Преобразовать секунды в минуты, часы и дни
if sec < MIN:
    print(f'{sec} sec')
elif sec >= MIN and sec < HOUR:
    minutes = sec // MIN
    seconds = sec % MIN
    print(f'{minutes:02d}:{seconds:02d}')
    print('mm:ss')
elif sec >= HOUR and sec < DAY:
    hours = sec // HOUR
    minutes = (sec - (HOUR * hours)) // MIN
    seconds = sec % MIN
    print(f'{hours:02d}:{minutes:02d}:{seconds:02d}')
    print('hh:mm:ss')
elif sec >= DAY:
    days = sec // DAY
    hours = (sec - (DAY * days)) // HOUR
    minutes = (sec - (DAY * days) - (HOUR * hours)) // MIN
    seconds = sec % MIN
    print(f'{days:02d}:{hours:02d}:{minutes:02d}:{seconds:02d}')
    print('dd:hh:mm:ss')