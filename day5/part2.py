import re

f1 = open("input.txt", "r")
text = f1.read()
f2 = open("output2.txt", "w")
mas = re.split('\n', text)

good = 0

def good_stroka1(stroka):
    global k1
    for i in range(len(stroka)-2):
        if stroka[i]==stroka[i+2]:
            k1 = 1
    return k1

def good_stroka2(stroka):
    global k2
    count = 0
    for i in range(len(stroka)):
        if stroka[i:i+2] in stroka[i+2:]:
            count += 1
    if count > 0:
        k2 = 1
    return k2

for i in mas:
    k1 = 0
    k2 = 0
    good_stroka1(i)
    good_stroka2(i)
    if k1 + k2 == 2:
       good += 1

f2.write(str(good))
f2.close
f1.close
