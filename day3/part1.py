f1 = open('input.txt', 'r')
f2 = open('output2.txt', 'w')
text = f1.read()
t1 = []
t2 = text[::2]
for i in text:
    if i not in t2:
        t1.append(i)
    
xy1 = [[0,0]]
x1 = 0
y1 = 0
x2 = 0
y2 = 0
p = 1

#Обычный санта
for i in t1:
    if i == '^':
        x1 += 1
    if i == 'v':
        x1 -= 1
    if i == '>':
        y1 += 1
    if i == '<':
        y1 -= 1
    if [x1,y1] not in xy1:
        p += 1
    xy1.append([x2,y2])

#Робо-Санта
for i in t2:
    if i == '^':
        x2 += 1
    if i == 'v':
        x2 -= 1
    if i == '>':
        y2 += 1
    if i == '<':
        y2 -= 1
    if [x2,y2] not in xy1:
        p += 1
        xy1.append([x2,y2])
    
f2.write(str(p))
f2.close()
f1.close()
    
