import re
import itertools

f1 = open("input.txt", "r")
text = f1.read()
f2 = open("output1.txt", "w")

nado = '1234567890qwertyuiopasdfghjklzxcvbnm'
nado2 = list(itertools.product(nado, repeat=2))
m = []
for i in range(len(nado2)):
    s = '\\x' + nado2[i][0]+ nado2[i][1]
    m.append(s)
    
text = re.split(r'\n', text)
counter1 = 0
counter2 = 0

for stroka in text:
    #stroka = stroka.strip()
    counter1 += len(stroka)
    stroka = stroka[1:-1]
    if r'\\' in stroka:
        stroka = stroka.replace(r'\\', '*')
    if r'\"' in stroka:
        stroka = stroka.replace(r'\"', '*')
    for r in m:
        if r in stroka:
            stroka = stroka.replace(r, '*')
    counter2 += len(stroka)

counter = counter1 - counter2
         
f2.write(str(counter))
f2.close
f1.close
