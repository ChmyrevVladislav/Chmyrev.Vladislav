f1 = open('input.txt', 'r')
text = f1.read()
f2 = open('output2.txt', "w")

x = 0
count = 0

for i in text:
    if i == '(':
        x += 1
        count +=1
    elif i == ')':
        x -= 1
        count +=1
    if x == -1:
        f2.write(str(count))
        f2.close()
        break

f1.close()
