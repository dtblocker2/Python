def factorial(n):
    i = 1
    x = 1
    while x <= n:
        i *= x
        x += 1
        if x == n+1:
            print(i)
    return x

factorial(69)