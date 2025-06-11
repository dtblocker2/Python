""""and or statement are same as logic gates 
for eg if I write condition_1 or condition_2 and condition_3
then python will first solve or statement between condition_1 and condition_2  and then their output will be solved by and statement with condition_3"""
#example is here
A = int(input("A: "))
G = input("M/F: ")
if A == 1 or A == 2 and G == "M":
    print("fee is 100")
elif A == 3 or A == 4 and G == "F":
    print("fee is 200")
elif A == 5 and G == "M":
    print("fee is 300")
else:
    print("no fee")