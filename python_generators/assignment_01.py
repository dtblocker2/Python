def square(num):
    i=1
    while i<=num:
        yield i**2
        i+=1

output = square(10000)

for i in output:
    print(i)