import random
print('Привет! Как тебя зовут?')
name = input()

def guess_number():
    print('Что ж, '+name+', я загадываю число от 1 до 20.')
    number = random.randint(1, 20)
    for col in range(6):
        print('Попробуй угадать:')
        your_number = int(input())
        if your_number > number:
            print('Твоё число слишком большое.')
        if your_number < number:
            print('Твоё число слишком маленькое.')
        if your_number == number:
            break

    if your_number == number:
        print('Отлично,'+name+'! Ты угадал за '+str(col+1)+' попыток')
    else:
        print('Извини, ты не угадал! Я загадал число ' + str(number))

play_again = 'да'
while play_again == 'да':
    guess_number()
    print('сыграем  еще?(да или нет)')
    play_again = input()
    play_again = play_again.lower()