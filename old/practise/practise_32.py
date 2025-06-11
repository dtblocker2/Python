#finding sum of first N natural numbers
n = int(input("write a ending natural number "))
x = 0
i = 0
while x <= n:
    i += x
    x += 1
    if i > 100000:
        print("don't put load on system nigga")
        break
    else:
        if x == n+1:
            print(i)