# Задача 107 Создайте программу для игры в ""Крестики-нолики"" (Добавьте игру против бота)

#инициализация игрового поля
import random as r
field = [1,2,3,
         4,5,6,
         7,8,9]

#вывод поля на экран
def print_field(field):
    print('-------------')
    print(f'| {field[0]} | {field[1]} | {field[2]} |')
    print('-------------')
    print(f'| {field[3]} | {field[4]} | {field[5]} |')
    print('-------------')
    print(f'| {field[6]} | {field[7]} | {field[8]} |')
    print('-------------')

#сочетания индексов для победы
victory = [(0, 1, 2),
           (3, 4, 5),
           (6, 7, 8),
           (0, 3, 6),
           (1, 4, 7),
           (2, 5, 8),
           (0, 4, 8),
           (2, 4, 6)]

#проверка наличия победителя
def chek_victory(field):
    if any(all(field[i] == 'X' for i in victory[j]) for j in range(8)):
        return 'X'
    if any(all(field[i] == 'O' for i in victory[j]) for j in range(8)):
        return 'O'
    return False

#сделать ход в ячейку
def step(symbol, f):
    while True:
        try:
            num = int(input(f'введите номер ячейки, в которую хотите поставить {symbol} >>> ')) - 1
            if num < 0 or num > 8: 
                raise Exception
            elif str(f[num]).isalpha():
                raise Exception
            f[num] = symbol
            return f
        except:
            print('Пожалуйста введите номер свободной ячейки')

# выбор хода для бота сложность студент
def bot_choice_student(field):
#если в ряду два O и нет Х
    for index in victory:
        if (field[index[0]], field[index[1]], field[index[2]]).count('O') == 2\
            and (field[index[0]], field[index[1]], field[index[2]]).count('X') == 0:
            temp = [i for i in (field[index[0]], field[index[1]], field[index[2]]) if i!='O'][0]
            field[temp - 1] = 'O'
            return
#если в ряду два X и нет О
    for index in victory:
        if (field[index[0]], field[index[1]], field[index[2]]).count('X') == 2\
            and (field[index[0]], field[index[1]], field[index[2]]).count('O') == 0:            
            temp = [i for i in (field[index[0]], field[index[1]], field[index[2]]) if i!='X'][0]
            field[temp - 1] = 'O'
            return
#в ряду один О и нет X
    for index in victory:
        if (field[index[0]], field[index[1]], field[index[2]]).count('X') == 0 \
            and (field[index[0]], field[index[1]], field[index[2]]).count('O') == 1:            
            temp = r.choice([i for i in (field[index[0]], field[index[1]], field[index[2]]) if i!='O'])
            field[temp - 1] = 'O'
            return
#для первого хода компьютера в центр или в правый верхний угол
    if 'O' not in field:
        if field[4] != 'X':
            field[4] = 'O'
        else:
            field[2] = 'O'
#для любого другого варианта
    else:
        temp = r.choice([i for i in field if not (i in ['X', 'O'])])
        field[temp - 1] = 'O'

# выбор хода для бота сложность школьник
def bot_choice_school(field):
#если в ряду два O и нет Х
    for index in victory:
        if (field[index[0]], field[index[1]], field[index[2]]).count('O') == 2\
            and (field[index[0]], field[index[1]], field[index[2]]).count('X') == 0:
            temp = [i for i in (field[index[0]], field[index[1]], field[index[2]]) if i!='O'][0]
            field[temp - 1] = 'O'
            return
#если в ряду два X и нет О
    for index in victory:
        if (field[index[0]], field[index[1]], field[index[2]]).count('X') == 2\
            and (field[index[0]], field[index[1]], field[index[2]]).count('O') == 0:            
            temp = [i for i in (field[index[0]], field[index[1]], field[index[2]]) if i!='X'][0]
            field[temp - 1] = 'O'
            return
    temp = r.choice([i for i in field if not (i in ['X', 'O'])])
    field[temp - 1] = 'O'

# выбор хода для бота сложность младенец
def bot_choice_baby(field):
    temp = r.choice([i for i in field if not (i in ['X', 'O'])])
    field[temp - 1] = 'O'


# Основная программа игрок против игрока
def PVP_mod():
    game_over = False
    player1 = True
    count = 0
    print_field(field)     # показываем карту

    while game_over == False and count < 9:
        # спрашиваем у игрока, куда делать ход
        if player1:
            symbol = "X"
            print("Игрок №1, ", end='')
            step(symbol, field) # делаем ход в указанную ячейку
            print_field(field)
        else:
            symbol = "O"
            print("Игрок №2, ", end='')
            step(symbol, field) # делаем ход в указанную ячейку
            print_field(field)
        count += 1
        win = chek_victory(field) # определим победителя
        if win:
            game_over = True

        player1 = not(player1)        
    
    # Игра окончена. Объявим результат. 
    if count > 8 and not game_over:
        print('Ничья!')
    elif win == 'X':       
        print("Победил, Игрок №1")
    else: print("Победил, Игрок №2")

# Основная программа игрок против бота
def AI_mod():
    game_over = False
    player1 = True
    count = 0
    while True:
        print('Выберите сложность игры: 1 - младенец, 2 - школьник, 3 - студент')
        try:
            n = int(input())
            if n not in [1, 2, 3]:
                raise Exception
            break
        except: 
            print('Для выбора уровня сложности нажмите 1, 2 или 3')
   
    print_field(field)     # показываем карту
    while game_over == False and count < 9:
        # спрашиваем у игрока, куда делать ход
        if player1:
            symbol = "X"
            print("Игрок, ", end='')
            step(symbol, field) # делаем ход в указанную ячейку
            print_field(field)
        else:
            symbol = "O"
            print('Ход бота')
            if n == 1:
                bot_choice_baby(field)
            elif n == 2:
                bot_choice_school(field)
            else:
                bot_choice_student(field)  # бот делает ход
            print_field(field)
        count += 1
        win = chek_victory(field) # определим победителя
        if win:
            game_over = True

        player1 = not(player1)        
    
    # Игра окончена. Объявим результат. 
    if count > 8 and not game_over:
        print('Ничья!')
    elif win == 'X':       
        print("Победил, Игрок")
    else: print("Победил, Бот")


print('''Крестики Нолики- это логическая игра между двумя противниками
на квадратном поле 3 на 3 клетки или большего размера. 
Один из игроков играет «крестиками», второй — «ноликами». 
Игроки по очереди ставят на свободные клетки поля 3х3 знаки.
Один всегда крестики, другой всегда нолики. Первый, выстроивший 
в ряд 3 своих фигуры по вертикали, горизонтали или диагонали, 
выигрывает. Первый ход делает игрок, ставящий крестики.
Если вы выбрали игру против компьютера, то вы ходите первым''')

# основной цикл
while True:
    print('Если вы хотите поиграть с другом (PVP) нажмите p или P')
    print('Если вы хотите поиграть против компьютера (AI) нажмите e или E')
    try:
        play = input()
        if not play in 'PpEeРрЕе' or len(play) > 1:
            raise Exception
        elif play in 'PpРр': PVP_mod()
        else: AI_mod()
        break
    except:
        print('Некорректный выбор, попробуйте еще раз!')
