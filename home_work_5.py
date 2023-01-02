# Домашнее задание Семинар 5* (сдавать только к семинару 5!)

# Задача 26:  
# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

# def my_pow(a, b):
#     if b >= 0:
#         if b == 0:
#             return 1
#         if b == 1:
#             return a
#         return a * my_pow(a, b - 1)
#     if b < 0:
#         if a == 0:
#             return '0 в отрицательной степени = неопределенность (1 / 0)'
#         if b == 0:
#             return 1
#         if b == -1:
#             return 1 / a
#         return (1 / a) * my_pow(a, b + 1)

# while True:
#     try:
#         A = int(input('Введите целое число для возведения степень >>> '))
#         B = int(input('Введите степень (целое число), в которую нужно возвести число >>> '))
#         break
#     except:
#         print('Вы ввели некорректное значение, необходимо ввести целые числа')

# print(my_pow(A, B))


# Задача 28:
# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# def my_sum(a, b):
#     if a == 0:
#         return b
#     elif b == 0:
#         return a
#     elif a >= b:
#         return 1 + my_sum(a, b - 1)
#     else: 
#         return 1 + my_sum(a - 1, b)
# while True:
#     try:
#         a = int(input('Введите первое целое неотрицательное число >>> '))
#         if a < 0: raise Exception
#         b = int(input('Введите второе целое неотрицательное число >>> '))
#         if b < 0: raise Exception
#         break
#     except:
#         print('Вы ввели некорректное значение, необходимо ввести целые неотрицательные числа')
# print(f'сумма целых неотрицательных чисел {a} и {b} равна {my_sum(a, b)}')

# Задачи на повторение по материалам предыдущих семинаров (по желанию)
# Задача 105 Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# def remove_piece_of_text(text, fragment='абв'):
#     return text.replace(fragment, '')

# Text = input('Введите текст >>> ')
# frag = input('Введите набор символов, который хотите удалить (значение по умолчанию "абв") >>> ')
# if frag:
#     print(f'Отредактированный текст без сочетания символов "{frag}">>> {remove_piece_of_text(Text, frag)}')
# else:
#     print('Отредактированный текст без "абв" >>>', remove_piece_of_text(Text))

# Задача 106 Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента? 
# (Добавьте игру против бота)

print(f'количество конфет, которое нужно взять первому игроку,\
чтобы забрать все конфеты у своего конкурента >>> {101 % (28 + 1)} штук')
import random as r

import csv
columns = ['name', 'wins', 'loses']

def get_rating(): #распечатать топ 10 игроков из итогового файла результаты
    with open('Results.csv', 'r', encoding='UTF-8') as f:
        d = sorted(list(csv.DictReader(f, delimiter=';')), key=lambda x: x['name'])
        count = 0
        print('ТОП 10 игроков:')
        for k in sorted(d, key=lambda x: (int(x['wins']), -int(x['loses'])), reverse=True):
            if count > 9: 
                break
            print(f"{count + 1}.) {k['name']} {k['wins']} {k['loses']}")
            count+=1

def update_rating(name, wins, loses): #обновить рейтинг в файле с результатами на основании результатов игры
    with open('Results.csv', 'r', encoding='UTF-8', newline='') as f:
        global columns
        d = list(csv.DictReader(f, delimiter=';'))
        if d:
            data = {d[i]['name']: {'wins': int(d[i]['wins']), 'loses': int(d[i]['loses'])} for i in range(len(d))}
            if name in data:
                data[name]['wins'] += wins
                data[name]['loses'] += loses
            else:
                data[name] = {'wins': wins, 'loses': loses}
        else:        
            data = {name: {'wins': wins, 'loses': loses}} 
        data_upd = [{'name': k, 'wins': data[k]['wins'], 'loses': data[k]['loses']}\
             for k in data if type(data[k]['wins']) == int]
    with open('Results.csv', 'w', encoding='UTF-8', newline='') as out:
        out.truncate()
        writer = csv.DictWriter(out, fieldnames=columns, delimiter=';')
        writer.writeheader()
        writer.writerows(data_upd)

def get_correct_input(name):  #корректность ввода количества конфет игроком
    while True:
        try:
            inp = int(input(f"{name} забирает >>> "))
            if inp > 28:
                print(f'Не жадничай, {name}! Ты не можешь взять так много!')
                raise Exception
            if inp <= 0:
                raise Exception           
            return inp
        except:
            print(f'Количество конфет должно быть в диапазоне от 1 до 28! Попробуй еще раз, {name}!')
            continue
#сообщения для продолжения хода
message = ['сколько конфет возьмешь?', \
'подумай хорошенько и бери конфеты.',\
'твоя очередь!', 'хвтай скорее конфетки)!', 'бери, не стесняйся!', 'твой ход, не спи!']

def P_v_P(): #игрок против игрока
    total = 101
    max_step = 28
    count = 0
    global message
    pl_1 = input('\nВведите имя первого игрока >>>  ')
    pl_2 = input('\nВведите имя второго игрока >>>  ')
    while pl_2 == pl_1:
        pl_2 = input('\nИмя второго игрока должно отличаться от имени первого {pl_1}')
    print(f'Да начнутся голодные игры {pl_1} против {pl_2}!')
    print(f'Сейчас Пресвятой Рандом определит того, кто ходит первым!')
    x = r.randint(1, 2)
    if x == 1:
        first = pl_1
        second = pl_2
    else:
        first = pl_2
        second = pl_1     
    print(f'Первым делает ход {first}, поздравляю!')  
    while total > 0:
        if not count % 2:
            print(f'{first}, {r.choice(message)}', end=' ')
            step = get_correct_input(first)
            while step > total:
                print('Вы хотите взять больше конфет, чем осталось!')
                step = get_correct_input(first)
            total -= step
            count += 1
            print(f'Поле хода №{count} конфет на столе осталось - {total} шт.')
        else:
            print(f'{second}, {r.choice(message)}', end=' ')
            step = get_correct_input(second)
            while step > total:
                print('Вы хотите взять больше конфет, чем осталось!')
                step = get_correct_input(second)
            total -= step
            count += 1
            print(f'Поле хода №{count} конфет на столе осталось - {total} шт.')            
    if count%2 == 0:
        print(f'Победителем стал {second}, поздравляю!')
        update_rating(second, 1, 0)
        update_rating(first, 0, 1)
    else:
        print(f'Победителем стал {first}, поздравляю!')
        update_rating(first, 1, 0)
        update_rating(second, 0, 1)
    print('Спасибо за игру!')



names = ['Железный человек', 'Автобот', 'Я-робот', 'Электроник',\
'R2D2', 'РоботФедор', 'Железяка', 'Компьютер']


def smart_choice(num, st):
    arr = [i for i in range(1, st + 1)]
    if num % (st + 1):
        #увеличиваем шанс выбора нужного числа конфет для компьютера
        arr.extend([num % (st + 1) for _ in range(1, (st + 1))]) 
        return r.choice(arr)
    else: 
        return r.choice(arr) #если пользователь просчитал ходы правильно, то выбирается просто рандомное число


def P_v_E(): #игрок против компьютера
    total = 101
    max_step = 28
    count = 0
    global message
    global names
    player = input('\nВведите свое имя >>>  ')
    comp = r.choice(names)
    if player == comp:
        comp += 'v01'
    print(f'Да начнутся голодные игры {player} против {comp}!')
    print(f'Сейчас Пресвятой Рандом определит того, кто ходит первым!')
    x = r.randint(1, 2)
    if x == 1:
        first = player
        second = comp
    else:
        first = comp
        second = player  
    print(f'Первым делает ход {first}, поздравляю!')  
    while total > 0:
        if (not count % 2) and first == player:
            print(f'{first}, {r.choice(message)}', end=' ')
            step = get_correct_input(first)
            while step > total:
                print('Вы хотите взять больше конфет, чем осталось!')
                step = get_correct_input(first)
            total -= step
            count += 1
            print(f'Поле хода №{count} конфет на столе осталось - {total} шт.')
        elif (not count % 2) and first == comp:
            if total <= 28:
                step = total
            else:
                step = smart_choice(total, 28)
            total -= step
            print(f'{first} забирает {step} шт.')
            count += 1
            print(f'Поле хода №{count} конфет на столе осталось - {total} шт.')
        elif count % 2 and second == player:
            print(f'{second}, {r.choice(message)}', end=' ')
            step = get_correct_input(second)
            while step > total:
                print('Вы хотите взять больше конфет, чем осталось!')
                step = get_correct_input(second)
            total -= step
            count += 1
            print(f'Поле хода №{count} конфет на столе осталось - {total} шт.')
        else:
            if total <= 28:
                step = total
            else:
                step = smart_choice(total, 28)
            total -= step
            print(f'{second} забирает {step} шт.')
            count += 1         
            print(f'Поле хода №{count} конфет на столе осталось - {total} шт.')    
    if count%2 == 0:
        print(f'Победителем стал {second}!') 
        update_rating(second, 1, 0)
        update_rating(first, 0, 1)
    else:
        print(f'Победителем стал {first}!')
        update_rating(first, 1, 0)
        update_rating(second, 0, 1)
    print('Спасибо за игру!')




print()
print('*'*50)
print('Добро пожаловать в игру 2021 конфета!')
print('Расскажу основные правила:')
print('''Эта игра предусмотрена для двух игроков\n
Я даю Вам 2021 конфету\n
Далее компьютер выбирает игрока, который будет брать конфеты первым.\n
За один ход можно взять минимум 1 и не более 28 конфет.\n
Кто забирает последние конфеты со стола, тот является победителем!\n
Впереди Вас ждет долгая и нудная игра\n
Начинаем...''')
print()
print('Для начала давай выберем, кто сегодня играет')

while True:
    print('Если вы хотите поиграть с другом (PVP) нажмите p или P')
    print('Если вы хотите поиграть против компьютера (PVE) нажмите e или E')
    try:
        play = input()
        if not play in 'PpEeРрЕе' or len(play) > 1:
            raise Exception
        elif play in 'PpРр': P_v_P()
        else: P_v_E()
        break
    except:
        print('Некорректный выбор, попробуйте еще раз!')
get_rating()       



# Задача 107 Создайте программу для игры в ""Крестики-нолики"" (Добавьте игру против бота)

# Задача 108 Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных (модуль в отдельном файле, импортируется как библиотека)
# метод Упаковка: на вход подается текстовый файл, на выходе текстовый файл со сжатием.
# метод Распаковка: на вход подается сжатый текстовый файл, на выходе текстовый файл восстановленный.
# Прикинуть достигаемую степень сжатия (отношение количества байт сжатого к исходному).