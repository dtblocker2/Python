a = 1
b = 2.93
sum_1 = a+b
#here python will automatically identify type of variable a and b. But in below case
c = "2"
d = 3
#sum_2 = c + d

print(sum_1)
#print(sum_2) #error
""" to solve above problem we type cast it ie forcefully change datatype of c byusing int(c) or float(c) or str(c)"""
f = float(c)
print(f + d)

"""obviously if c = "dhruva" then it would not converted into int or float by above method"""