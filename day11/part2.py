f1 = open("input.txt", "r")
f2 = open("output1.txt", "w")
text = f1.read()

def increase_string(string):
    curr_index = len(string) - 1
    string = string[:curr_index] + chr(ord(string[curr_index]) + 1) + string[curr_index+1:]
    while string[curr_index] > 'z':
        string = string[:curr_index] + 'a' + string[curr_index+1:]
        curr_index -= 1
        string = string[:curr_index] + chr(ord(string[curr_index]) + 1) + string[curr_index+1:]
    return string

def contains_three_increasing(string):
    prev = None
    count = 0
    for char in string:
        if prev is None or ord(char) == ord(prev) + 1:
            count += 1
        else:
            count = 1
        if count == 3:
            return True
        prev = char
    return False

def contains_two_pairs(string):
    pairs = []
    prev = None
    for char in string:
        if char == prev and char not in pairs:
            pairs.append(char)
        prev = char
    return len(pairs) >= 2

def generate_new_password(stroka):
    valid = False
    evil_letters = ["i", "o", "l"]
    while not valid:
        valid = True
        stroka = increase_string(stroka)
        if not contains_three_increasing(stroka):
            valid = False
            continue
        for evil_letter in evil_letters:
            if evil_letter in stroka:
                valid = False
                break
        if not valid:
            continue
        if not contains_two_pairs(stroka):
            valid = False
            continue
    return stroka

text = generate_new_password(text)
text = generate_new_password(text)

f2.write(str(text))
f2.close
f1.close
