# а - дозапись, w - перезапись, r - чтение.
f = open('zhenya.txt', 'r')


for i in range(5):
    line = f.readline()
    print(line, end='')

f.close()
