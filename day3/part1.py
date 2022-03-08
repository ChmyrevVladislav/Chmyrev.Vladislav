f1 = open('input.txt', 'r')
f2 = open('output2.txt', 'w')
text = f1.read()
    
xy1 = [[0,0]]
x1 = 0
y1 = 0 
p = 1

#Обычный санта
for i in text:
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
    xy1.append([x1,y1])
    
f2.write(str(p))
f2.close()
f1.close()
