from random import randint
from time import sleep
def intro():
    print('''Вы находитесь в землях, заселенных драконами.
    Перед собой вы видите две пещеры.
    В одной из них - дружелюбный дракон,
    который готов поделиться с вами сокровищами.
    Во второй - жадный и голодный дракон, который мигом вас съест.''')


def select_cave():
    print('В какую пещеру вы войдете? (нажмите клавишу 1 или 2)')
    selected_cave = int(input())
    return selected_cave


def cheek_cave(selected_cave):
    friendly_cave = randint(1, 2)
    print('Вы приближаетесь к пещере...')
    sleep(1)
    print('Её темнота заставляет дрожать вас')
    sleep(1)
    print('Большой дракон выпрыгивает перед вами! Он раскрывает свою пасть и...')
    sleep(1)
    if selected_cave == friendly_cave:
        print('Делится с вами своими сокровищами!')
    else:
        print('Моментально вас съедает!')

play_again = 'да'
while play_again == 'да':
    intro()
    sleep(2)
    cheek_cave(select_cave())
    print('Сыграем  еще? (да или нет)')
    play_again = input()

