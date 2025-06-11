import math
import time
i = int(input("enter the last number: "))
lol = []

for j in range(1,i+1):
    if ((math.factorial(j-1) + 1)/j) % 1 == 0:
        lol.append(j)

print("Prime numbers from 1 and", i, "are", lol)
time.sleep(10)