# Задача 26:  
# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

def my_pow(a, b):
    if b >= 0:
        if b == 0:
            return 1
        if b == 1:
            return a
        return a * my_pow(a, b - 1)
    if b < 0:
        if a == 0:
            return '0 в отрицательной степени = неопределенность (1 / 0)'
        if b == 0:
            return 1
        if b == -1:
            return 1 / a
        return (1 / a) * my_pow(a, b + 1)

while True:
    try:
        A = int(input('Введите целое число для возведения степень >>> '))
        B = int(input('Введите степень (целое число), в которую нужно возвести число >>> '))
        break
    except:
        print('Вы ввели некорректное значение, необходимо ввести целые числа')

print(my_pow(A, B))