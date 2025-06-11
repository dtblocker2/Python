#for loops are used for sequential traversal ie for traversing list, string, tuples etc.
lol = [1, 2, "kaku", 4, 5, 6]
#also applicable to lol = (1, 2, "kaku", 4, 5, 6)

for element in lol:
    print(element)
else: #optional
    print("end")

name = input("enter your name")
for char in name:
    if char == "a" or "A":
        print("name has letter 'A'")
        break
else:
    print("name doesn't have letter 'A'")