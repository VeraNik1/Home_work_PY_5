# Задача 106 Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента? 
# (Добавьте игру против бота)

print(f'количество конфет, которое нужно взять первому игроку,\
чтобы забрать все конфеты у своего конкурента >>> {2021 % (28 + 1)} штук')
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
            print(f"{count + 1}.){k['name']} - побед:  {k['wins']} - поражений: {k['loses']}")
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
    total = 2021
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
        first = True
        print(f'Первым делает ход {pl_1}, поздравляю!')
    else:
        first = False 
        print(f'Первым делает ход {pl_2}, поздравляю!')
    while total > 0:
        if first:
            print(f'{pl_1}, {r.choice(message)}', end=' ')
            step = get_correct_input(pl_1)
            while step > total:
                print('Вы хотите взять больше конфет, чем осталось!')
                step = get_correct_input(pl_1)
            total -= step
            count += 1    
            print(f'Поле хода №{count} конфет на столе осталось - {total} шт.')
        else:
            print(f'{pl_2}, {r.choice(message)}', end=' ')
            step = get_correct_input(pl_2)
            while step > total:
                print('Вы хотите взять больше конфет, чем осталось!')
                step = get_correct_input(pl_2)
            total -= step
            count += 1
            print(f'Поле хода №{count} конфет на столе осталось - {total} шт.')
        first = not(first)            
    if first:
        print(f'Победителем стал {pl_2}, поздравляю!')
        update_rating(pl_2, 1, 0)
        update_rating(pl_1, 0, 1)
    else:
        print(f'Победителем стал {pl_1}, поздравляю!')
        update_rating(pl_1, 1, 0)
        update_rating(pl_2, 0, 1)
    print('Спасибо за игру!')



names = ['Железный человек', 'Автобот', 'Я-робот', 'Электроник',\
'R2D2', 'РоботФедор', 'Железяка', 'Компьютер']

#выбор количества конфет для компьютера
def smart_choice(num, st):
    arr = [i for i in range(1, st + 1)]
    if num % (st + 1):
        #увеличиваем шанс выбора нужного числа конфет для компьютера
        arr.extend([num % (st + 1) for _ in range(1, (st + 1))]) 
        return r.choice(arr)
    else: 
        return r.choice(arr) #если пользователь просчитал ходы правильно, то выбирается просто рандомное число


def P_v_E(): #игрок против компьютера
    total = 2021
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
        player1 = True
        print(f'Первым делает ход {player}, поздравляю!')
    else: 
        player1 = False 
        print(f'Первым делает ход {comp}')
    while total > 0:
        if player1:
            print(f'{player}, {r.choice(message)}', end=' ')
            step = get_correct_input(player)
            while step > total:
                print('Вы хотите взять больше конфет, чем осталось!')
                step = get_correct_input(player)
            total -= step
            count += 1
            print(f'Поле хода №{count} конфет на столе осталось - {total} шт.')
        else:
            if total <= 28:
                step = total
            else:
                step = smart_choice(total, 28)
            total -= step
            print(f'{comp} забирает {step} шт.')
            count += 1
            print(f'Поле хода №{count} конфет на столе осталось - {total} шт.')
        player1 = not(player1)
    if not player1:
        print(f'Победителем стал {player}!') 
        update_rating(player, 1, 0)
        update_rating(comp, 0, 1)
    else:
        print(f'Победителем стал {comp}!')
        update_rating(comp, 1, 0)
        update_rating(player, 0, 1)
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