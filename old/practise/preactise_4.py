def sum(n):
    if n == 0:
        return 0
    else:
        p = n + sum(n-1)
        return p

print(sum(3))