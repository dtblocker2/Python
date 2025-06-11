lol = "\nthis text was not originally present in the file it was appended by the python program append.py"
with open("test_2.txt", "a") as file:
    file.write(lol)
    print("operation done successfully")
