BOT_TOKEN_FILENAME = 'token.txt'

# символы, которые используются
SYMBOL_X = '❎'
SYMBOL_O = '🅾'
SYMBOL_UNDEF = '⬜'

# ответы бота
ANSW_YOUR_TURN = 'Yor turn'
ANSW_YOU_WIN = 'You are a winner!'
ANSW_BOT_WIN = 'The Bot won('
ANSW_DRAW = 'Draw!'
ANSW_HELP = 'Tic-tac-toe game bot\n\n' \
'''
Send /new_game to start a new game\n
'''
# уровни сложности
ANSW_BOT_REGIM = 'Выберите сложность игры: 1 - младенец, 2 - школьник, 3 - студент'



# ошибки
ALERT_CANNOT_MOVE_TO_THIS_CELL = 'You can press only ' + SYMBOL_UNDEF
ALERT_ABOUT_TOKEN = 'Please, make in the project folder file "token.txt"\
             and put your token there, then run the script one more time'