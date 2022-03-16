import re

f1 = open('input.txt', 'r')
f2 = open('output1.txt','w')
text = f1.read()
mas = re.split('\n', text)

good = 0

#первое условие
def good_stroka1(stroka):
    global k1
    count = 0
    for n in range(len(stroka)):
        if stroka[n] in 'euioa':
            count += 1
        if count >= 3:
            k1 = 1
    return k1

#второе условие
def good_stroka2(stroka):
    global k2
    for n in range(len(stroka)-1):
        if stroka[n] == stroka[n+1]:
            k2 = 1
    return k2

#третье условие
def good_stroka3(stroka):
    global k3
    k3 = 0
    if not 'ab' in stroka:
        if not 'cd' in stroka:
            if not 'pq' in stroka:
                 if not 'xy' in stroka:
                    k3 = 1
    return k3

for i in mas:
    k1 = 0
    k2 = 0
    k3 = 0
    good_stroka1(i)
    good_stroka2(i)
    good_stroka3(i)
    if k1 + k2 + k3 == 3:
       good += 1
    
f2.write(str(good))
f2.close
f1.close
