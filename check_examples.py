f = open('examples.txt', 'r')
line = f.readline()

while line:
    splited_line = line.split()
    digit1, sigh, digit2 = splited_line

    if sigh =='+':
        answer = int(digit1) + int(digit2)
    if sigh =='-':
        answer = int(digit1) - int(digit2)

    print(digit1, sigh, digit2, '=', answer)
    line = f.readline()
