#palindrome means that a list/word is same in forward and reverse order ex- maam, racecar
lol = [1, 2, 3, 2]

lol_2 =lol.copy()
lol_2.reverse()

if lol_2 == lol:
    print("list is palidrome")
else:
    print("it is not palidrome")