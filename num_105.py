# Задача 105 Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

def remove_piece_of_text(text, fragment='абв'):
    return text.replace(fragment, '')

Text = input('Введите текст >>> ')
frag = input('Введите набор символов, который хотите удалить (значение по умолчанию "абв") >>> ')
if frag:
    print(f'Отредактированный текст без сочетания символов "{frag}">>> {remove_piece_of_text(Text, frag)}')
else:
    print('Отредактированный текст без "абв" >>>', remove_piece_of_text(Text))