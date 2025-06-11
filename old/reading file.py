with open('text.txt') as file:
    print(file.read())
    print(file.closed) #here in this identation file is open
#but as we change indentation the file is closed so no reading can be done now
print(file.closed)
'''print(file.read())''' #as you can see this will give error