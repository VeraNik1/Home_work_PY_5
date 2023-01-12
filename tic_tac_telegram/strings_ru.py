BOT_TOKEN_FILENAME = 'token.txt'

# символы, которые используются
SYMBOL_X = '❎'
SYMBOL_O = '🅾'
SYMBOL_UNDEF = '⬜'

# ответы бота
ANSW_YOUR_TURN = 'Ваш ход'
ANSW_YOU_WIN = 'Вы победили!'
ANSW_BOT_WIN = 'Победил бот('
ANSW_DRAW = 'Ничья'
ANSW_HELP = 'Бот для игры в крестики-нолики\n\n' \
'''
Используйте команду /new_game для начала новой игры\n
'''
# уровни сложности
ANSW_BOT_REGIM = 'Выберите сложность игры: 1 - младенец, 2 - школьник, 3 - студент'



# ошибки
ALERT_CANNOT_MOVE_TO_THIS_CELL = 'Нажимать можно только на ' + SYMBOL_UNDEF
ALERT_ABOUT_TOKEN = 'Пожалуйста, создайте в папке проекта файл "token.txt"\
             и поместите туда токен для работы телеграм бота  и запустите скрипт заново'