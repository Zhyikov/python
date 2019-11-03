print('Привет! Меня зовут Роджер. А как тебя?')
name = input()
name = name.title()
print('Приятно познакомиться, '+name)
print('''Давай проверим твои знания в математике
Ты готов?(да или нет)''')
ready = input()
ready = ready.lower()

while ready not in {'да', 'нет'}:
    print('''Должно быть да или нет.
Введи заново''')
    ready = input()
    ready = ready.lower()

if ready == 'да':
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


else:
    print('''Передумал? Хорошо, может как-нибудь в следующий раз...
Пока!''')

