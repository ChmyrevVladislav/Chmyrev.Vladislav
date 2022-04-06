import re

f1 = open('input.txt', 'r')
f2 = open('output1.txt', 'w')
text = f1.read()

commands = re.split(r'\n', text)

setka = []

for x in range(1000):
    for y in range(1000):
        setka.append([x,y,0])

for i in range(len(commands)):
    com = re.split(',''|''\s', commands[i])
    if com[0] == 'turn':
        x1 = int(com[2])
        y1 = int(com[3])
        x2 = int(com[5])
        y2 = int(com[6])
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                if com[1] == 'on':
                    setka[1000*x+y][2] = 1
                else:
                    setka[1000*x+y][2] = 0
    elif com[0] == 'toggle':
        x1 = int(com[1])
        y1 = int(com[2])
        x2 = int(com[4])
        y2 = int(com[5])
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                if setka[1000*x+y][2] == 1:
                    setka[1000*x+y][2] = 0
                else:
                    setka[1000*x+y][2] = 1
    else:
        print("Неверный ввод")

count = 0
for i in setka:
    if i[2] == 1:
        count +=1

f2.write(str(count))
f2.close
f1.close
