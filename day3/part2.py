f1 = open('input.txt', 'r')
f2 = open('output2.txt', 'w')
text = f1.read()
    
xy = [[0,0]]
x1 = 0
y1 = 0
x2 = 0
y2 = 0
p = 1

#Обычный санта
for i in range (len(text)):
    if i % 2 == 0:
        #Обычный санта
        if text[i] == '^':
            x1 += 1
        if text[i] == 'v':
            x1 -= 1
        if text[i] == '>':
            y1 += 1
        if text[i] == '<':
            y1 -= 1
        if [x1,y1] not in xy:
            p += 1
        xy.append([x1,y1])
    else:
        if text[i] == '^':
            x2 += 1
        if text[i] == 'v':
            x2 -= 1
        if text[i] == '>':
            y2 += 1
        if text[i] == '<':
            y2 -= 1
        if [x2,y2] not in xy:
            p += 1
        xy.append([x2,y2])
    
f2.write(str(p))
f2.close()
f1.close()
    
