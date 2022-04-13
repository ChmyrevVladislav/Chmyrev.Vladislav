import re
import itertools

f1 = open("input.txt", "r")
text = f1.read()
f2 = open("output1.txt", "w")

# Создание типо графа
m = []
cities = []
d = []

m1 = re.split(r'\n', text)
for el in m1:
    m2 = re.split(' to ''|'' = ', el)
    m.append(m2)

for el in m:
    if el[0] not in cities:
        cities.append(el[0])
    if el[1] not in cities:
        cities.append(el[1])
        
# Составление путей
puti = list(itertools.permutations(cities))
for put in puti:
    d1 = 0
    for x in range (len(cities)-1):
        for y in range(len(m)):
            if (put[x] == m[y][0] or put[x] == m[y][1]) and (put[x+1] == m[y][0] or put[x+1] == m[y][1]):
                d1 += int(m[y][2])
    d.append(d1)

f2.write(str(min(d)))
f2.close
f1.close


