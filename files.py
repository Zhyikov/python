# а - дозапись(add), w - перезапись(write), r - чтение(read).
f = open('zhenya.txt', 'r')


for i in range(5):
    line = f.readline()
    print(line, end='')

f.close()
