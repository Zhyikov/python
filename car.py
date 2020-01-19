print('Введите команду:')
command = input()
engine_status = ''


while command:

    while command not in {'help', 'on', 'off', 'exit'}:
        print('Такой команды не существует')
        command = input()

    if command == 'help':
        print('''on - завести двигатель
off - заглушить двигатель
exit - выйти''')
    if command == 'on':
        if engine_status:
            print('Двигатель уже заведён')
        else:
            print('Завожу двигатель')
            engine_status = True
        if command == 'off':
        if engine_status:
            print('Глушу двигатель')
            engine_status = False
        else:
            print('Двигатель уже заглушен')

    if command == 'exit':
        print('Выхожу')
        break

    print('Введите команду:')
    command = input()
