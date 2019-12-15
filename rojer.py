from random import randint, choice
from timeit import default_timer


def select_mode():
    print('''
    1 - тренировка
    0 - выход
''')
    mode = int(input())
    return mode


def time_endings(digit):
    if digit == 11:
        return ''
    else:
        last_digit = str(digit)
        if last_digit == '1':
            return 'у'
        elif 1 < int(last_digit) < 5:
            return 'ы'
        else:
            return ''


def seconds_convert(time_in_seconds):
    if time_in_seconds < 60:
        spent = f'{time_in_seconds} секунд{time_endings(time_in_seconds)}'
    else:
        minutes = time_in_seconds//60
        seconds = time_in_seconds - (minutes*60)

        if seconds == 0:
            spent = f'{minutes} минут{time_endings(minutes)}'
        else:
            spent = f'{minutes} минут{time_endings(minutes)} и {seconds} секунд{time_endings(seconds)}'

    return spent


def training():

    print('Давай проверим твои знания в математике.')

    print('Хорошо')
    print(f'{name}, сколько примеров ты готов решить?')

    questions_quantity = input()
    while not questions_quantity.isdigit():
        print('Должна быть цифра!')
        questions_quantity = input()

    print(f'До скольки будем считать?')
    max_answer = input()
    while not max_answer.isdigit():
        print('Должна быть цифра!')
        max_answer = input()
    print('Хорошо, тогда начинаем...')

    correct_answers = 0
    fails = 0
    spent_time = 0


    for i in range(int(questions_quantity)):
        print(f'Пример {i+1}:')

        number1 = randint(1, int(max_answer))
        number2 = randint(1, int(max_answer))
        sign = choice('+-')



        if sign == '-':
            while number1 < number2:
                number1 = randint(1, int(max_answer))
                number2 = randint(1, int(max_answer))
            correct_answer = number1 - number2


        if sign == '+':
            while number1 + number2 > int(max_answer):
                number1 = randint(1, int(max_answer))
                number2 = randint(1, int(max_answer))
            correct_answer = number1 + number2

        print(f'Сколько будет {number1} {sign} {number2}?')
        start = default_timer()
        answer = input('Введи ответ:\n')
        stop = default_timer()
        spent_time += round(stop - start)

        if int(answer) == correct_answer:
            print('Правильно!')
            correct_answers += 1
        else:
            f = open(f'{name}.errors', 'a')
            f.write(f'{number1} {sign} {number2}\n')
            f.close()
            fails += 1
            print(f'''Неправильно!
    Правильный ответ: {correct_answer}''')

    if fails != 0:
        print(f'''Правильных ответов: {correct_answers}
    Ошибок: {fails}
    Затрачено времени: {seconds_convert(spent_time)}''')
    else:
        print(f'Ты решил без ошибок за {seconds_convert(spent_time)}')

#Основной блок программы
print('Привет! Меня зовут Роджер. А как тебя?')
name = input()
name = name.title()
print('Приятно познакомиться, '+name)

#цикл повторяется бесконечно
while True:

    mode = select_mode()
    if mode == 1:
        training()
    elif mode == 0:
        print('Пока!')
        break
    else:
#пусто(ничего), так не будет жаловаться
        pass


