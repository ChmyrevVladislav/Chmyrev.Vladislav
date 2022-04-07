f1 = open("input.txt", "r")
text = f1.read()
f2 = open("output1.txt", "w")

def game(text):
    stroka = ''
    count = 1
    for i in range(len(text)-1):
        if text[i] == text[i+1]:
            count += 1
        else:
            stroka += str(count) + text[i]
            count = 1
    return stroka

for i in range (40):
    text += 'p'
    total = game(text)
    text = total

f2.write(str(len(total)))
f2.close
f1.close
