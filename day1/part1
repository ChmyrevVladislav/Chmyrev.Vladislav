f1 = open('input.txt', 'r')
text = f1.read()
f2 = open('output1.txt', "w")

x = 0

for i in text:
  if i == '(':
    x += 1
  elif i == ')':
    x -= 1
  else:
    print ("Неправильный ввод данных")
    
f2.write(str(x))
f2.close()
