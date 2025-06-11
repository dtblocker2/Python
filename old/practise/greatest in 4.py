a = float(input("a="))
b = float(input("b="))
c = float(input("c="))
d = float(input("d="))

if a>b and a>c and a>d:
    print("a is greatest")
elif b>c and b>d:
    print("b is greatest")
elif c>d:
    print("c is greatest")
else:
    print("d is greatest")