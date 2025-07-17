""" here is how to make global variables just like javascript """

counter = 0
def increase():
    global counter
    # counter = 0
    counter +=1

increase()
print(counter)