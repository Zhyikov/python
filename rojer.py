from random import randint, choice

print('Привет! Меня зовут Роджер. А как тебя?')
name = input()
name = name.title()
print('Приятно познакомиться, '+name)
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

for i in range(int(questions_quantity)):
    print(f'Пример {i+1}:')

    number1 = randint(1, int(max_answer))
    number2 = randint(1, int(max_answer))
    sign = choice('+-')
    print(f'Сколько будет {number1} {sign} {number2}?')

    if sign == '-':
        while number1 < number2:
            number1 = randint(1, int(max_answer))
            number2 = randint(1, int(max_answer))

    if sign == '+':
        while number1 + number2 > int(max_answer):
            number1 = randint(1, int(max_answer))
            number2 = randint(1, int(max_answer))