#using function repeatedly to form a loop

def nigga(n):
    if n == 0:
        return
    print(n)
    nigga(n-1)

nigga(9)