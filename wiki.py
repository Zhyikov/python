import wikipedia
wikipedia.set_lang('ru')
while True:
    try:
        search = input('Что нужно найти?\n')
        s = wikipedia.page(search)
        print(s.content)
    except:
        print('По вашему запросу ничего не найдено!')
        print()
        print('Допустимые варинаты:')
        print('====================')
        s = wikipedia.search(search)
        for item in s:
            print(item)
        print('====================')
        print()