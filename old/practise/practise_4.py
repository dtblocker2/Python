#finding factorial first N natural numbers
n = int(input("write a ending natural number "))
i = 1
for x in range(1, n+1):
    i *= x
    if x == n:
        if i < 10**1000:
            print(i)
        else:
            print("you broke the system nigga")