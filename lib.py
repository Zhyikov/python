def check_input(user_input: str, allowed_values: list, user_message: str = 'Попробуй еще раз:\n') -> str:



    while user_input not in allowed_values:

        allowed_str = ''
        for item in allowed_values[:-1]:
            allowed_str += f'{item},'

        allowed_str = allowed_str[:-2]
        allowed_str = f'{allowed_str} или {allowed_values[-1]}'
        print('Должно быть', allowed_str)
        user_input = input(user_message)

    return user_input

