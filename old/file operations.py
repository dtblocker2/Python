import os

lol = "C:\\Users\\hp\\Desktop\\text.txt"

if os.path.exists(lol):
    print("it is already created")
    if os.path.isfile(lol):
        print("and it is file")
    else:
        print("it is not a file (it can be folder)")
else:
    print("no its not created")
    y = input("do you want to created it")

if y == "yes" or "y":
    pass
elif y == "no" or "n":
    print("file won't be created")