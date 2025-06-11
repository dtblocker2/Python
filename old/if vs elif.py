num = 5
#if we use only if statement and not elif then the result of all conditions will be displayed
if num>2:
    print("number is greater than 2")
if num>3:
    print("number is greater than 3")
if num > 4:
    print("number is greater than 4")

#if we use only elif statement then only first fullfilled statement will be shown
if num>2:
    print("number is greater than 2")
elif num>3:
    print("number is greater than 3") #see python has skipped this statement
if num > 4:
    print("number is greater than 4") #but python hasn't skipped this statement