# Задача 28:
# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

def my_sum(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    elif a >= b:
        return 1 + my_sum(a, b - 1)
    else: 
        return 1 + my_sum(a - 1, b)
while True:
    try:
        a = int(input('Введите первое целое неотрицательное число >>> '))
        if a < 0: raise Exception
        b = int(input('Введите второе целое неотрицательное число >>> '))
        if b < 0: raise Exception
        break
    except:
        print('Вы ввели некорректное значение, необходимо ввести целые неотрицательные числа')
print(f'сумма целых неотрицательных чисел {a} и {b} равна {my_sum(a, b)}')


