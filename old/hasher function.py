import random
import time

def hasher(text):
    lst = list(text)
    lst_2 = []
    y = random.randint(0,9)
    lst_2.append(str(y))
    for i in lst:
        if (ord(i)+y) <= 126:
            lst_2.append(chr(ord(i)+y))
            y += 1
        else:
            lst_2.append(chr((ord(i)+y)%94+33))
            y += 1
    return "".join(lst_2)

text = input('enter pass')
print(hasher(text))
time.sleep(10)