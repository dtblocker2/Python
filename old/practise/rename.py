import os
while True:
    x = input("enter name of song: ")
    try:
        os.rename('C:\\Users\\dhruv\\Music\\spotifydown.com - '+x+'.mp3', "C:\\Users\\dhruv\\Music\\"+x+".mp3")
        print("operation done sucessfully")
    except FileNotFoundError:
        print("file not found")
    y = input("Add Another song? ")
    if y == "no":
        break
print("the function has stopped. Thanks for using this service")