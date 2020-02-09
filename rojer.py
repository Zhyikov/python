from random import randint, choice
from timeit import default_timer
import os


def select_mode():
    if os.path.exists(f'{name}_errors.txt'):
            print('''
        1 - тренировка
        2 - работа над ошибками
        0 - выход
    ''')
    else:
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

    questions_number = 0
    unique_examples = []
    unique_combinatious = int(max_answer)**2


    for i in range(int(questions_quantity)):

        print(f"попытка {i}")
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


        example = f'{number1} {sign} {number2}'
        if example not in unique_examples:
            unique_examples.append(example)
            questions_number +=1

            print(f'Пример {questions_number}:')
            print(f'Сколько будет {example}?')
            start = default_timer()
            answer = input('Введи ответ:\n')
            stop = default_timer()
            spent_time += round(stop - start)

            if int(answer) == correct_answer:
                print('Правильно!')
                correct_answers += 1
            else:
                f = open(f'{name}_errors.txt', 'a')
                f.write(f'{number1} {sign} {number2} 3\n')
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


def errors_handling(file_name):
    with open(file_name, 'r') as f1, open(f'tmp_{file_name}', 'a') as f2:

        correct_answers = 0
        fails = 0
        spent_time = 0

        for line in f1:
            line = line.split()
            number1, sign, number2, correct_answers_to_solve = line

            number1 = int(number1)
            number2 = int(number2)
            correct_answers_to_solve = int(correct_answers_to_solve)

            if sign == '-':
                correct_answer = number1 - number2

            if sign == '+':        
                correct_answer = number1 + number2
            
            print('Сколько будет ', number1, sign, number2, '?')
            start = default_timer()
            answer = input('Введи ответ:\n')
            stop = default_timer()
            spent_time += round(stop - start)

            if int(answer) == correct_answer:
                if correct_answers_to_solve > 1:
                    f2.write(f'{number1} {sign} {number2} {correct_answers_to_solve}\n')
                print('Правильно!')
                correct_answers += 1
            else:
                f2.write(f'{number1} {sign} {number2} {correct_answers_to_solve-1}\n')
                fails += 1
                print(f'''Неправильно!
        Правильный ответ: {correct_answer}''')
    os.remove(file_name)
    if os.getsize(f'tmp_{file_name}') > 0:
        os.rename(f'tmp_{file_name}', file_name)
    else:
        os.renove(f'tmp_{file_name}') 

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
    elif mode == 2:
        errors_handling(f'{name}_errors.txt')
    else:
#пусто(ничего), так не будет жаловаться
        pass