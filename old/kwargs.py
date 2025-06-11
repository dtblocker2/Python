# **kwargs  =   parameter will pack all arguments into a dictionary
#                useful so that a function can accept avarying amount of keyword arguments

def intro(**lol):
    print("hello" + " " + lol["first"] + " " + lol["last"])

intro(first = "Dhruva", middle = "majoka", last = "kumar")

#in order to print full name
def hello(**lol_2):
    print("hello", end =" ")
    for key,value in lol_2.items():
        print(value, end=" ")

hello(title="Mr.",first="dhruva",last="majoka")