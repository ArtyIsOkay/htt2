import curses
import random
import time

def matrix_rain(stdscr):
    # Настройка экрана
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)
    
    # Зелёные цвета Matrix
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)  # Яркий зелёный
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)  # Обычный зелёный
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_GREEN)  # Чёрный на зелёном
    
    # Аутентичные символы Matrix (катакана, латиница, цифры)
    symbols = [
        # Катакана (основные символы из фильма)
        "ア", "イ", "ウ", "エ", "オ",
        "カ", "キ", "ク", "ケ", "コ",
        "サ", "シ", "ス", "セ", "ソ",
        "タ", "チ", "ツ", "テ", "ト",
        "ナ", "ニ", "ヌ", "ネ", "ノ",
        "ハ", "ヒ", "フ", "ヘ", "ホ",
        "マ", "ミ", "ム", "メ", "モ",
        "ヤ", "ユ", "ヨ",
        "ラ", "リ", "ル", "レ", "ロ",
        "ワ", "ヲ", "ン",
        
        # Латинские буквы и цифры
        "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
        "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
        "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
        "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
        
        # Специальные символы
        "@", "#", "$", "%", "&", "*", "+", "-", "=", "~", "|",
        "<", ">", "/", "\\", ":", ";", "?", "!", "."
    ]
    
    # Главный цикл анимации
    while True:
        # Получаем размеры терминала КАЖДЫЙ КАДР
        height, width = stdscr.getmaxyx()
        
        # Инициализируем капли при первом запуске или изменении размера
        if not hasattr(matrix_rain, 'drops') or len(matrix_rain.drops) != width:
            matrix_rain.drops = []
            for i in range(width):
                matrix_rain.drops.append({
                    'pos': random.randint(-height * 2, 0),
                    'speed': random.uniform(0.5, 1.5),
                    'length': random.randint(5, 20),
                    'chars': []
                })
        
        # Проверка нажатия клавиши для выхода
        if stdscr.getch() in (ord('q'), 27):
            break
        
        # Очистка экрана
        stdscr.clear()
        
        # Обновление и отрисовка капель
        for x in range(min(width, len(matrix_rain.drops))):
            drop = matrix_rain.drops[x]
            
            # Обновляем позицию
            drop['pos'] += drop['speed']
            
            # Если капля ушла за экран - создаем новую
            if drop['pos'] - drop['length'] > height:
                drop['pos'] = random.randint(-height * 2, 0)
                drop['speed'] = random.uniform(0.5, 1.5)
                drop['length'] = random.randint(5, 20)
                drop['chars'] = []
            
            # Добавляем новый символ в хвост
            if drop['pos'] > -5:
                new_char = random.choice(symbols)
                drop['chars'].insert(0, new_char)
                if len(drop['chars']) > drop['length']:
                    drop['chars'].pop()
            
            # Отрисовываем каплю с ПРОВЕРКОЙ ГРАНИЦ
            for i, char in enumerate(drop['chars']):
                y = int(drop['pos'] - i)
                
                # Двойная проверка границ
                if 0 <= y < height and 0 <= x < width:
                    try:
                        if i == 0:  # Голова - ярко-зелёная
                            stdscr.addstr(y, x, char, curses.color_pair(1) | curses.A_BOLD)
                        elif i < len(drop['chars']) // 3:  # Верх хвоста - обычный зелёный
                            stdscr.addstr(y, x, char, curses.color_pair(2) | curses.A_BOLD)
                        elif i < 2 * len(drop['chars']) // 3:  # Середина - зелёный
                            stdscr.addstr(y, x, char, curses.color_pair(2))
                        else:  # Низ хвоста - тёмно-зелёный
                            stdscr.addstr(y, x, char, curses.color_pair(2) | curses.A_DIM)
                    except curses.error:
                        pass  # Игнорируем ошибки отрисовки
        
        # Информационная строка (только если есть место)
        if width > 40 and height > 5:
            try:
                info_text = " MATRIX SYSTEM ACTIVE | PRESS 'Q' TO EXIT "
                start_x = max(0, (width - len(info_text)) // 2)
                stdscr.addstr(height-2, start_x, info_text, curses.color_pair(3))
            except curses.error:
                pass
        
        stdscr.refresh()
        time.sleep(0.05)

# Запуск программы
if __name__ == "__main__":
    try:
        print("Запуск Matrix-симуляции...")
        print("Используйте терминал в полноэкранном режиме для лучшего эффекта!")
        print("Для выхода нажмите 'Q' или ESC\n")
        time.sleep(2)
        curses.wrapper(matrix_rain)
    except KeyboardInterrupt:
        pass
    finally:
        print("\n" + "="*50)
        print("СИМУЛЯЦИЯ ЗАВЕРШЕНА")
        print("Возвращайтесь в реальность...")
        print("="*50)