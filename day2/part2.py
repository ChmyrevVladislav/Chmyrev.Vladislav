import re

f1 = open("input.txt", "r")
f2 = open("output2.txt", "w")
text = f1.read()

#Небольшие преобразования, чтобы получить удобный для работы список
p = re.split('x''|''\n', text)
a = []
for i in (p):
    i = int(i)
    a.append(i)

S = 0
lsum = 0

for i in range(0, len(a), 3):
    a = int(p[i])
    b = int(p[i+1])
    c = int(p[i+2])
    s1 = a*b
    s2 = a*c
    s3 = b*c
    s = 2*s1 + 2*s2 + 2*s3 + min(s1, s2, s3)
    S += s
    #лента
    l = min(2*a+2*b, 2*a+2*c, 2*b+2*c) + a*b*c
    lsum += l

f2.write(str(lsum))
f2.close()
f1.close()
    



