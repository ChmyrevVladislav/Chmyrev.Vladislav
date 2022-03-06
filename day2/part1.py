import re

f1 = open("input.txt", "r")
f2 = open("output1.txt", "w")
text = f1.read()

#Небольшие преобразования, чтобы получить удобный для работы список
p = re.split('x''|''\n', text)
a = []
for i in (p):
    i = int(i)
    a.append(i)

S = 0

for i in range(0, len(a), 3):
    a = int(p[i])
    b = int(p[i+1])
    c = int(p[i+2])
    s1 = a*b
    s2 = a*c
    s3 = b*c
    s = 2*s1 + 2*s2 + 2*s3 + min(s1, s2, s3)
    S += s
    
'''
И тут я что-то не понял прикола. После удаление всех символов кроме чисел в файле,
я сделал новый список и стал добавлять туда данные типа integer.
Но когда я стал обрабатывать его в цикле for, возникла ошибка "can't multiply sequence by non-int of type 'str'".
Если не сложно будет, можете пожалуйста объяснить что не так? :)
'''

f2.write(str(S))
f2.close()
f1.close()
    



