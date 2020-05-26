class TooMuchArgsError(Exception):
    def __init__(self, text):
        self.txt = text

try:
    phrase = (input().split(' '))
    if len(phrase) > 3:
        raise TooMuchArgsError('Слишком много аргументов!')
except TooMuchArgsError as e:
    print(e)
else:
    try:
        list_operations = ['+', '-', '*', '/']
        assert phrase[0] in  list_operations, 'Неверная операция'

        if phrase[0] == '+':
            print(f'Сумма чисел равна: {int(phrase[1]) + int(phrase[2])}')
        elif phrase[0] == '-':
            print(f'Разность чисел равна {int(phrase[1]) - int(phrase[2])}')
        elif phrase[0] == '*':
            print(f'Произведение чисел равно {int(phrase[1]) * int(phrase[2])}')
        elif phrase[0] == '/':
            print(f'Частное {int(phrase[1])} от {int(phrase[2])} равно {int(phrase[1]) / int(phrase[2])}')

    except ZeroDivisionError:
        print('На нуль делить нельзя')
    except TypeError:
        print('Ошибка типа')
