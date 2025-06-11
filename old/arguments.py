#to perform a function on idefinite amount of variables

def add(*lol):
    sum = 0
    for i in lol:
        sum += i
    return sum

print(add(1, 2, 3, 4, 5, 6, 7))