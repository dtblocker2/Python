text = "kaku is at home \nand the file is completely overwritten"
with open('test.txt', 'w') as lol: #w means file is open in writable format
    lol.write(text)
    print("file overwritten sucessfully")